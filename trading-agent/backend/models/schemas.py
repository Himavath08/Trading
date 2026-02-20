from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional, Any
from backend.models.db_models import JobStatus

class AnalyzeRequest(BaseModel):
    ticker: str                         # e.g. "AAPL"
    force_refresh: bool = False         # Skip cache and re-run

class JobResponse(BaseModel):
    job_id: UUID
    ticker: str
    status: JobStatus
    message: str

class ResultResponse(BaseModel):
    job_id: UUID
    ticker: str
    status: JobStatus
    result: Optional[Any] = None        # Investment memo dict
    error: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class HistoryResponse(BaseModel):
    jobs: list[ResultResponse]
    total: int