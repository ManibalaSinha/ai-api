from pydantic import BaseModel
from typing import Optional

class QueryRequest(BaseModel):
    query: str
    user_id: Optional[str] = None

class QueryResponse(BaseModel):
    answer: str
    source: Optional[str] = None
    latency: float
