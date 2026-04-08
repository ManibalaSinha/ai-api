from fastapi import APIRouter
from app.models.schemas import QueryRequest, QueryResponse
from app.services.agent_service import agent
from app.utils.logger import log_request, log_response

router = APIRouter()

@router.post("/ask", response_model=QueryResponse)
async def ask_question(request: QueryRequest):
    log_data = log_request(request.query)

    result = agent(request.query)

    log_data = log_response(log_data, result)

    return QueryResponse(
        answer=result,
        latency=log_data["latency"]
    )
