from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from app.utils.config import embeddings, llm

# Sample documents (replace later with DB/files)
raw_docs = [
    "Python is a programming language",
    "FastAPI is used for building APIs",
    "RAG means Retrieval Augmented Generation"
]

# Convert to Documents
documents = [Document(page_content=doc) for doc in raw_docs]

# Split docs
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=10)
docs = text_splitter.split_documents(documents)

# Vector DB
vectorstore = Chroma.from_documents(docs, embeddings)

def rag_pipeline(query: str):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    retrieved_docs = retriever.get_relevant_documents(query)
    context = "\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
    Use ONLY this context to answer:
    {context}

    Question: {query}
    """

    response = llm.invoke(prompt)
    return response.content

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
