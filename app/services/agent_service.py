from app.services.rag_service import rag_pipeline
from app.services.llm_service import call_llm

def agent(query: str):
    query_lower = query.lower()

    if "document" in query_lower or "rag" in query_lower:
        return rag_pipeline(query)

    elif "hello" in query_lower:
        return "Hi! How can I help you?"

    else:
        return call_llm(query)
