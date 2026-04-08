from app.services.llm_service import call_llm
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langsmith import traceable
from app.utils.config import llm
from app.services.rag_service import rag_pipeline

# Define tools
tools = [
    Tool(
        name="RAG Search",
        func=rag_pipeline,
        description="Use this for answering questions from documents"
    )
]

# Initialize agent
agent_executor = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

@traceable(name="Agent Execution", metadata={"type": "orchestration"})
def agent(query: str):
    return agent_executor.run(query)
