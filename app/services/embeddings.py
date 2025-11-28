import os
from typing import List
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text(file_path: str) -> str:
    """
    Simplified: extract text from PDF or TXT
    """
    ext = os.path.splitext(file_path)[1].lower()
    text = ""
    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    elif ext == ".pdf":
        from PyPDF2 import PdfReader
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    else:
        raise ValueError("Unsupported file type")
    return text

def chunk_text(text: str, chunk_size: int = 500) -> List[str]:
    """
    Simple chunking by words
    """
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))
    return chunks

def embed_text(text: str) -> List[float]:
    """
    Generate embeddings using OpenAI
    """
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return response.data[0].embedding
