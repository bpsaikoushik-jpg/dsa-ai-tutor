import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai


env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

api_key = os.getenv("GEMINI_API_KEY", "").strip()
if not api_key:
    raise ValueError(
        "Gemini API key not found. Copy .env.example to .env and set GEMINI_API_KEY."
    )

client = genai.Client(api_key=api_key)
for model in client.models.list():
    if "generateContent" in (model.supported_actions or []):
        print(model.name)
