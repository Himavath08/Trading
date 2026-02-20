import asyncio
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from backend.database import get_db
from backend.models.db_models import AnalysisJob, JobStatus
from backend.models.schemas import AnalyzeRequest, JobResponse
from backend.services.agent_runner import run_agent_pipeline

router = APIRouter()

@router.post("/analyze", response_model=JobResponse, status_code=202)
async def trigger_analysis(
    body: AnalyzeRequest,
    db: AsyncSession = Depends(get_db)
):
    ticker = body.ticker.upper().strip()

    # Optional: check if recent result exists (cache hit)
    if not body.force_refresh:
        existing = await db.execute(
            select(AnalysisJob)
            .where(AnalysisJob.ticker == ticker, AnalysisJob.status == JobStatus.completed)
            .order_by(AnalysisJob.created_at.desc())
        )
        cached = existing.scalars().first()
        if cached:
            return JobResponse(
                job_id=cached.id,
                ticker=ticker,
                status=cached.status,
                message="Returning cached result. Use force_refresh=true to re-run."
            )

    # Create new job row
    job = AnalysisJob(ticker=ticker, status=JobStatus.pending)
    db.add(job)
    await db.commit()
    await db.refresh(job)

    # Fire-and-forget background task (asyncio approach — no Celery needed to start)
    asyncio.create_task(run_agent_pipeline(job.id, ticker, db))

    return JobResponse(
        job_id=job.id,
        ticker=ticker,
        status=JobStatus.pending,
        message="Analysis started. Poll /results/{job_id} for updates."
    )