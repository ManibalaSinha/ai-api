from typing import List, Tuple
from app.services import embeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Simple in-memory store
VECTOR_DB = []
METADATA = []

def add_chunks(chunks: List[str]) -> List[int]:
    ids = []
    for chunk in chunks:
        emb = embeddings.embed_text(chunk)
        VECTOR_DB.append(emb)
        METADATA.append(chunk)
        ids.append(len(VECTOR_DB) - 1)
    return ids

def search_vector(query: str, top_k: int = 3) -> List[Tuple[str, float]]:
    query_emb = np.array(embeddings.embed_text(query)).reshape(1, -1)
    vectors = np.array(VECTOR_DB)
    sims = cosine_similarity(query_emb, vectors)[0]
    top_indices = sims.argsort()[-top_k:][::-1]
    return [(METADATA[i], float(sims[i])) for i in top_indices]
