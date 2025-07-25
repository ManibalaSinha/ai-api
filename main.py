import asyncio,os, io, httpx, sys, torch, traceback, threading
import chardet, uvicorn
from PIL import Image
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, Header, HTTPException, File, UploadFile, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.security import APIKeyHeader
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from transformers import BlipProcessor, BlipForConditionalGeneration
from models.caption import generate_caption  # This must be defined in caption.py
from models.caption import get_image_captioning_model
from pydantic import BaseModel

app = FastAPI() # Create FastAPI
class TextInput(BaseModel):
    text: str

#  Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
ENABLE_IMAGE_CAPTIONING = os.getenv("ENABLE_IMAGE_CAPTIONING", "false").lower() == "true"

__huggingface__ = app
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
processor = None
model = None

def load_captioning_model():
    global processor, model
    if processor is None or model is None:
        processor, model = get_image_captioning_model()

#  Allow frontend requests (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# API Key Auth Middleware
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

def verify_api_key(x_api_key: str = Security(api_key_header)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")

# Base route
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <h2> Image Caption + Text Summarizer API is running!</h2>
    <p>POST your file to <code>/summarize</code></p>
    <p>POST your image to <code>/caption</code></p>
    """
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
@app.post("/summarize-text")
async def summarize_text_input(input: TextInput):
    try:
        summary = summarizer(input.text[:1024])[0]["summary_text"]
        return {"summary": summary}
    except Exception as e:
        return {"error": f"Summarization failed: {str(e)}"}


# Summarization endpoint
@app.post("/summarize")
async def summarize_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        detected = chardet.detect(contents)
        encoding = detected["encoding"]

        if not encoding:
            return {"error": "Could not detect file encoding"}

        text = contents.decode(encoding)
        if not text.strip():
            return {"error": "Uploaded file is empty or unreadable."}

        summary = summarizer(text[:1024])[0]["summary_text"]
        return {"summary": summary}
    except Exception as e:
        return {"error": f"Summarization failed: {str(e)}"}

@app.post("/caption", dependencies=[Depends(verify_api_key)])
async def caption_image(file: UploadFile = File(...)):
    if not ENABLE_IMAGE_CAPTIONING:
        return {"caption": "Image captioning is disabled on this instance."}

    contents = await file.read()
    try:
        image = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception as e:
        return {"error": f"Failed to open image: {str(e)}"}

        # Lazy-load the model
    load_captioning_model()

    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)

    print(" Caption generated:", caption) 

    return {"caption": caption}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.on_event("startup")
def warmup_model_in_background():
    if ENABLE_IMAGE_CAPTIONING:
        threading.Thread(target=load_captioning_model, daemon=True).start()

@app.on_event("startup")
async def keep_alive():
    async def ping_self():
        while True:
            try:
                async with httpx.AsyncClient() as client:
                    await client.get("http://localhost:8000/")
            except:
                pass
            await asyncio.sleep(60)  # ping every 60 seconds
    asyncio.create_task(ping_self())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
