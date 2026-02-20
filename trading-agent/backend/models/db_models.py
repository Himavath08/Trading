import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, JSON, Enum
from sqlalchemy.dialects.postgresql import UUID
from backend.database import Base
import enum

class JobStatus(str, enum.Enum):
    pending   = "pending"
    running   = "running"
    completed = "completed"
    failed    = "failed"

class AnalysisJob(Base):
    __tablename__ = "analysis_jobs"

    id         = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ticker     = Column(String(10), nullable=False, index=True)
    status     = Column(Enum(JobStatus), default=JobStatus.pending, nullable=False)
    result     = Column(JSON, nullable=True)        # Final investment memo
    error      = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)