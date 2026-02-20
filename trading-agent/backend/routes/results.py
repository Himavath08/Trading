from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from backend.database import get_db
from backend.models.db_models import AnalysisJob
from backend.models.schemas import ResultResponse

router = APIRouter()

@router.get("/results/{job_id}", response_model=ResultResponse)
async def get_results(job_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(AnalysisJob).where(AnalysisJob.id == job_id))
    job = result.scalars().first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return job