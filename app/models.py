from sqlalchemy import Column, Integer, String, Enum, DateTime, func
import enum
from .db import Base


class IncidentStatus(str, enum.Enum):
    NEW = "new"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    status = Column(Enum(IncidentStatus), nullable=False, default=IncidentStatus.NEW)
    source = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
