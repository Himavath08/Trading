import asyncio
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.models.db_models import AnalysisJob, JobStatus

# ── Import YOUR Phase 1 agents here ──────────────────────────────
# from agents.financial_agent import run_financial_analysis
# from agents.sentiment_agent import run_sentiment_analysis
# from agents.memo_agent import generate_memo
# ─────────────────────────────────────────────────────────────────

async def run_agent_pipeline(job_id: UUID, ticker: str, db: AsyncSession):
    """
    Core pipeline: runs all agents and saves result to DB.
    Called by Celery worker OR directly via asyncio background task.
    """
    try:
        # 1. Mark job as RUNNING
        await _update_job(db, job_id, status=JobStatus.running)

        # 2. ── Run your Phase 1 agents ──────────────────────────
        # Replace these placeholders with your actual agent calls
        
        financial_data = await asyncio.to_thread(
            lambda: {"revenue": "...", "eps": "..."}   # replace with: run_financial_analysis(ticker)
        )
        sentiment_data = await asyncio.to_thread(
            lambda: {"sentiment": "bullish"}           # replace with: run_sentiment_analysis(ticker)
        )
        memo = await asyncio.to_thread(
            lambda: {                                   # replace with: generate_memo(financial_data, sentiment_data)
                "ticker": ticker,
                "recommendation": "BUY",
                "summary": "Strong fundamentals...",
                "financial": financial_data,
                "sentiment": sentiment_data,
            }
        )
        # ────────────────────────────────────────────────────────

        # 3. Save result
        await _update_job(db, job_id, status=JobStatus.completed, result=memo)
        return memo

    except Exception as e:
        await _update_job(db, job_id, status=JobStatus.failed, error=str(e))
        raise

async def _update_job(db: AsyncSession, job_id: UUID, **kwargs):
    result = await db.execute(select(AnalysisJob).where(AnalysisJob.id == job_id))
    job = result.scalar_one()
    for key, val in kwargs.items():
        setattr(job, key, val)
    await db.commit()