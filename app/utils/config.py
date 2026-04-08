from langchain_openai import OpenAIEmbeddings, ChatOpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = "gpt-4o-mini"

# LangChain LLM
llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=MODEL_NAME,
    temperature=0
)

# Embeddings
embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
