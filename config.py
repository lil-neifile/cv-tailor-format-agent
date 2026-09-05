import os
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")
load_dotenv(ROOT  / "../.env")

llm_api_key = os.getenv("GEMINI_API_KEY")
model_primary = os.getenv("MODEL_PRIMARY")
model_backup = os.getenv("MODEL_BACKUP")

template_name = "html_template.html"
TEMPLATES_DIR = Path(__file__).resolve().parents[0] / "templates"