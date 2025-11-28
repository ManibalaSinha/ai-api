from fastapi import APIRouter, UploadFile, File
from app.services import embeddings, vector_store
import os

router = APIRouter()

UPLOAD_FOLDER = "uploaded_docs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Extract text (simplified for now)
    text = embeddings.extract_text(file_path)

    # Chunk and embed
    chunks = embeddings.chunk_text(text)
    ids = vector_store.add_chunks(chunks)

    return {"filename": file.filename, "chunks_added": len(chunks), "vector_ids": ids}
