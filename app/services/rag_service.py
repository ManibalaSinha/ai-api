# Mock RAG replace with FAISS/Chroma

documents = [
    "Python is a programming language",
    "FastAPI is used for APIs",
    "RAG stands for Retrieval Augmented Generation"
]

def retrieve_docs(query: str):
    return [doc for doc in documents if query.lower() in doc.lower()]

def rag_pipeline(query: str):
    context = retrieve_docs(query)
    context_text = "\n".join(context)

    prompt = f"""
    Answer based on context:
    {context_text}

    Question: {query}
    """

    from app.services.llm_service import call_llm
    return call_llm(prompt)
