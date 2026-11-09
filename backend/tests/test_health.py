"""phase 0 tests for health endpoint"""

from fastapi.testclient import TestClient

from app.config import settings
from app.main import app

client = TestClient(app)


def test_health_reports_ok_and_database():
    """needs Docker PostgresSQL running"""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["database_ok"] is True
    assert body["groq_model"] == settings.groq_model


def test_health_does_not_leak_secrets():
    response = client.get("/api/v1/health")
    if settings.groq_api_key:
        assert settings.groq_api_key not in response.text
    assert "password" not in response.text.lower()


def test_swagger_doce_open():
    response = client.get("/docs")
    assert response.status_code == 200
