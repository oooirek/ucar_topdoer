from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from .. import schemas, crud
from ..db import get_db

router = APIRouter(prefix="/incidents", tags=["incidents"])


@router.post("/", response_model=schemas.IncidentOut)
async def create_incident(payload: schemas.IncidentCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_incident(db, payload)


@router.get("/", response_model=list[schemas.IncidentOut])
async def list_incidents(status: Optional[schemas.IncidentStatus] = Query(None), db: AsyncSession = Depends(get_db)):
    return await crud.list_incidents(db, status)


@router.patch("/{incident_id}", response_model=schemas.IncidentOut)
async def update_incident_status(incident_id: int, payload: schemas.IncidentUpdate, db: AsyncSession = Depends(get_db)):
    return await crud.update_status(db, incident_id, payload.status)
