from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    app_name: str
    environment: str
    database_ok: bool
    groq_key_configured: bool
    groq_model: str
