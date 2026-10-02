import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

ROOT = Path(__file__).resolve().parents[0]
load_dotenv(ROOT / ".env")

class Config(BaseSettings):
    LLM_API_KEY: str = os.getenv("GEMINI_API_KEY")
    MODEL_PRIMARY: str = os.getenv("MODEL_PRIMARY")
    MODEL_BACKUP: str = os.getenv("MODEL_BACKUP")
    TEMPLATE_NAME: str = "html_template.html"
    TEMPLATES_DIR: Path = ROOT / "templates"

config = Config()