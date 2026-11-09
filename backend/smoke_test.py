"""Throwaway smoke test: one call to Groq. Delete in Phase 8."""

from groq import Groq

from app.config import settings

if not settings.groq_key_configured:
    raise SystemExit("GROQ_API_KEY is not set in backend/.env")

client = Groq(api_key=settings.groq_api_key)
response = client.chat.completions.create(
    model=settings.groq_model,
    messages=[
        {"role": "user", "content": "Reply with exactly: NovaMart smoke test OK"}
    ],
    max_tokens=500,
)
choice = response.choices[0]
print("Model:", settings.groq_model)
print("Reply:", choice.message.content)
print("Finish reason:", choice.finish_reason)
