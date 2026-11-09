"""Application settings. The only file that reads environment variables."""

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

# backend/ folder (config.py lives in backend/app/)
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

_PLACEHOLDER_KEY = "your-groq-api-key-here"


@dataclass(frozen=True)
class Settings:
    app_env: str
    app_name: str
    tenant_id: str
    database_url: str
    groq_api_key: str
    groq_model: str

    @property
    def groq_key_configured(self) -> bool:
        return bool(self.groq_api_key) and self.groq_api_key != _PLACEHOLDER_KEY


def get_settings() -> Settings:
    return Settings(
        app_env=os.getenv("APP_ENV", "development"),
        app_name=os.getenv("APP_NAME", "NovaMart AI Support"),
        tenant_id=os.getenv("TENANT_ID", "novamart"),
        database_url=os.getenv("DATABASE_URL", ""),
        groq_api_key=os.getenv("GROQ_API_KEY", ""),
        groq_model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
    )


settings = get_settings()
