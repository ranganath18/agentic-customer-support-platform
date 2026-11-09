"""Application entry point"""

from fastapi import FastAPI

from app.api.v1 import health
from app.config import settings

app = FastAPI(title=settings.app_name, version="0.1.0")
app.include_router(health.router, prefix="/api/v1")
