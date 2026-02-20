from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from backend.database import get_db
from backend.models.db_models import AnalysisJob
from backend.models.schemas import HistoryResponse, ResultResponse

router = APIRouter()

@router.get("/history", response_model=HistoryResponse)
async def get_history(
    db: AsyncSession = Depends(get_db),
    limit: int = Query(default=20, le=100),
    offset: int = Query(default=0)
):
    # Total count
    count_result = await db.execute(select(func.count(AnalysisJob.id)))
    total = count_result.scalar()

    # Paginated jobs
    jobs_result = await db.execute(
        select(AnalysisJob)
        .order_by(AnalysisJob.created_at.desc())
        .limit(limit)
        .offset(offset)
    )
    jobs = jobs_result.scalars().all()

    return HistoryResponse(jobs=jobs, total=total)