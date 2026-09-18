# CV Tailor Format Agent

A LangGraph agent that rewrites an AI Engineering CV to match a job description, renders it as styled HTML and a downloadable PDF, then cheers you on (and jokingly roasts you) for the keywords you hit or missed.

The Streamlit app in `main.py` is the main way to run it: upload a PDF CV, paste a job description, click **Tailor CV**, preview the result, and download the PDF.

## How it works

The uploaded CV is parsed to text with [Docling](https://github.com/docling-project/docling) (`src/services/cv_parser.py`). That text and the job description are loaded into agent state up front. Tools read that state themselves, so the model never has to paste a CV into a tool argument.

The agent loops between an LLM node and a tool node until the work is done:

1. **`tailor_cv`** — rewrite the CV against the job description (structured output: header, summary, experience, skills, education, plus matched / missing keywords).
2. **`build_html`** — render the tailored sections through the Jinja2 template in `templates/html_template.html`.
3. **`build_pdf`** — print that HTML to A4 PDF with Playwright.
4. **`inspire_applicant`** / **`fry_applicant`** — Gen-Z pep talk for matched keywords, humorous roast for missing ones.

If a tool is called out of order, it tells the model which prerequisite to run first.

LLM and tool nodes retry twice. The LLM node times out after 30s idle; the tool node after 120s. Chat and structured calls go through LiteLLM with a primary model and a backup if the primary fails.

Tailoring rules (from the system prompt): keep existing sections, swap in the job’s wording for overlapping skills, rewrite the summary, and translate the CV to Spanish when the job description is in Spanish.

## Project layout

```
main.py                 Streamlit UI (PDF upload + job description)
config.py               Env vars, model names, template path
src/
  workflow_agent.py     LangGraph graph (compile + retry/timeout policies)
  schemas.py            Pydantic models for the tailored CV
  agent/
    state_agent.py      Agent state (CV, JD, artifacts)
    nodes_agent.py      LLM node, ToolNode, continue/end routing
    tools.py            tailor / HTML / PDF / inspire / fry tools
    prompts_agent.py    System prompts
  services/
    llm.py              LiteLLM client with primary → backup fallback
    cv_parser.py        Docling PDF → text
    pdf_builder.py      Jinja2 HTML + Playwright PDF
templates/
  html_template.html    Resume layout
tests/                  Unit tests and a scripted agent walkthrough
```

## Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)
- A Gemini API key (via LiteLLM)
- Playwright Chromium (for PDF export)

## Setup

```bash
uv sync
uv run playwright install chromium
```

Create a `.env` in the project root:

```env
GEMINI_API_KEY=your-key
MODEL_PRIMARY=gemini/gemini-2.5-flash
MODEL_BACKUP=gemini/gemini-2.0-flash
```

## Run the app

```bash
uv run streamlit run main.py
```

Upload a PDF CV, paste a job description, and click **Tailor CV**. You get:

- A downloadable `tailored_cv.pdf`
- An HTML preview of the resume
- **Fry Applicant** and **Inspire Applicant** commentary

## Call the agent directly

The graph expects CV text, not a PDF. Parse first if you have a file:

```python
from src.workflow_agent import compiled_agent
from src.services.cv_parser import CVParser

cv_text = CVParser().parse(open("my_cv.pdf", "rb").read())

result = compiled_agent.invoke({
    "cv": cv_text,
    "job_description": open("job.txt").read(),
})

result["html_content"]         # styled HTML
result["pdf_bytes"]            # PDF bytes
result["keywords_matched"]
result["keywords_not_matched"]
result["inspiration"]
result["mock"]
```

## Tests

```bash
uv run pytest
```

`tests/verify_agent.py` walks the compiled graph with a scripted model (no live LLM, fake PDF) to check the happy path and the out-of-order tool guard:

```bash
uv run python tests/verify_agent.py
```
