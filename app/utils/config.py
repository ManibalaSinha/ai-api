from langchain_openai import OpenAIEmbeddings, ChatOpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "false")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "default")

# debug flag
DEBUG = True

MODEL_NAME = "gpt-4o-mini"

# LangChain LLM
llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=MODEL_NAME,
    temperature=0
)

# Embeddings
embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
