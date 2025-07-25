import io
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from functools import lru_cache

# 🐢 Lazy-load only once
processor = None
model = None

@lru_cache()
def get_image_captioning_model():
    global processor, model
    if processor is None or model is None:
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

def generate_caption(image_bytes: bytes) -> str:
    try:
        # Load and convert image
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        
        # Get captioning model
        processor, model = get_image_captioning_model()
        
        # Run captioning
        inputs = processor(image, return_tensors="pt")
        output = model.generate(**inputs)
        caption = processor.decode(output[0], skip_special_tokens=True)
        
        return caption
    except Exception as e:
        raise RuntimeError(f"Caption generation failed: {str(e)}")