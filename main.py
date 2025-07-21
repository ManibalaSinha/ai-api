import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, Header, HTTPException

from models.summarizer import summarize_text
from models.caption import generate_caption
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import UploadFile, File

# 🔒 Load secrets from .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = FastAPI()

# (Optional) Allow frontend React requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Reusable API key verification dependency
def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")

@app.get("/")
def home():
    return {"message": "Welcome to AI API!"}

@app.post("/summarize", dependencies=[Depends(verify_api_key)])
def summarize_text_route(payload: dict):
    text = payload.get("text")
    if not text:
        return JSONResponse(status_code=400, content={"error": "Missing 'text'"})
    result = summarize_text(text)
    return {"summary": result}

@app.post("/caption", dependencies=[Depends(verify_api_key)])
async def caption_image_route(file: UploadFile = File(...)):
    image_bytes = await file.read()
    caption = generate_caption(image_bytes)
    return {"caption": caption}
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Render provides the PORT env variable
    uvicorn.run("main:app", host="0.0.0.0", port=port)