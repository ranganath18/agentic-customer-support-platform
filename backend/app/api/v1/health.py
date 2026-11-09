from fastapi import APIRouter

from app.config import settings
from app.db.session import check_database
from app.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    database_ok = check_database()
    return HealthResponse(
        status="ok" if database_ok else "degraded",
        app_name=settings.app_name,
        environment=settings.app_env,
        database_ok=database_ok,
        groq_key_configured=settings.groq_key_configured,
        groq_model=settings.groq_model,
    )
