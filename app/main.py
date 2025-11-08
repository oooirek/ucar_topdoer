from fastapi import FastAPI
from .db import engine, Base
from .routers import incidents

app = FastAPI(title="Incident API")
app.include_router(incidents.router)


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
