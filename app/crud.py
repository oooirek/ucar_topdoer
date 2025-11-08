from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from . import models, schemas


async def create_incident(db: AsyncSession, data: schemas.IncidentCreate):
    obj = models.Incident(description=data.description, source=data.source)
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def list_incidents(db: AsyncSession, status_filter: str | None = None):
    query = select(models.Incident)
    if status_filter:
        query = query.where(models.Incident.status == status_filter)
    result = await db.execute(query)
    return result.scalars().all()


async def update_status(db: AsyncSession, incident_id: int, status_value: str):
    result = await db.execute(select(models.Incident).where(models.Incident.id == incident_id))
    obj = result.scalar_one_or_none()
    if not obj:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Incident not found")
    obj.status = status_value
    await db.commit()
    await db.refresh(obj)
    return obj
