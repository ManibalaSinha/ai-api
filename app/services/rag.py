from app.services import vector_store, embeddings
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def query_documents(query: str) -> tuple[str, list]:
    """
    Retrieve top chunks and generate final answer from LLM
    """
    top_chunks = vector_store.search_vector(query, top_k=3)
    context_text = "\n".join([chunk for chunk, _ in top_chunks])

    prompt = f"""
    You are a helpful assistant. Use the following context to answer the question.

    Context:
    {context_text}

    Question:
    {query}

    Answer:
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message["content"]
    return answer, [chunk for chunk, _ in top_chunks]
