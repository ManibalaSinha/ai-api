import io
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# 🐢 Lazy-load only once
processor = None
model = None

def get_image_captioning_model():
    global processor, model
    if processor is None or model is None:
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

def generate_caption(image_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    processor, model = get_image_captioning_model()
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True)

