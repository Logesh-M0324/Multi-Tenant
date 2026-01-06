from contextlib import asynccontextmanager
from core.database import connect_db, close_db
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app : FastAPI):

    await connect_db()

    yield

    await close_db()