import openai
import os
from transformers import pipeline, BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import io

# Set OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    print("Warning: OpenAI API key not set. Skipping OpenAI API calls.")

# Lazy initialization placeholders
_summarizer = None
_processor = None
_model = None

def summarize_text(text: str) -> str:
    global _summarizer
    if not openai.api_key:
        return "Summarization not available (API key missing)."
    
    if _summarizer is None:
        _summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

    summary = _summarizer(text, max_length=50, min_length=10, do_sample=False)
    return summary[0]['summary_text']


def generate_caption(image_bytes: bytes) -> str:
    global _processor, _model

    if _processor is None or _model is None:
        _processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        _model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    inputs = _processor(image, return_tensors="pt")
    out = _model.generate(**inputs)
    return _processor.decode(out[0], skip_special_tokens=True)
