from fastapi import APIRouter, Query
from app.services import rag

router = APIRouter()

@router.get("/")
def search(query: str = Query(..., min_length=1)):
    """
    Search uploaded documents using RAG pipeline
    """
    answer, source_docs = rag.query_documents(query)
    return {"query": query, "answer": answer, "sources": source_docs}
