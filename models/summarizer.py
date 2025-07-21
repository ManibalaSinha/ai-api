import openai
import os
from transformers import pipeline
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import io

# Set OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    print("Warning: OpenAI API key not set. Skipping OpenAI API calls.")
    # You can set a flag here if you want to conditionally handle this elsewhere
else:
    # You can place any OpenAI specific setup here if needed
    pass

# Initialize summarizer pipeline (Hugging Face model, no OpenAI dependency)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text: str) -> str:
    if not openai.api_key:
        # Fallback: maybe just return original text or a message
        return "Summarization not available (API key missing)."
    # If you want to call OpenAI here instead, wrap it similarly
    summary = summarizer(text, max_length=50, min_length=10, do_sample=False)
    return summary[0]['summary_text']

# Initialize image captioning models
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True)
