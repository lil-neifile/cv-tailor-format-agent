# CV Tailor Format Agent

A LangGraph agent that rewrites a CV to match an AI Engineering job description, renders it as styled HTML and a downloadable PDF, then cheers you on (and jokingly roasts you) for the keywords you hit or missed.

The Streamlit app in `main.py` is the main way to run it: paste a job description, click **Tailor CV**, preview the result, and download the PDF.

## How it works

The applicant CV and job description are loaded into agent state up front. Tools read that state themselves, so the model never has to paste a CV into a tool argument.

The agent loops between an LLM node and a tool node until the work is done:

1. **`tailor_cv`** — rewrite the CV against the job description (structured output: header, summary, experience, skills, education, plus matched / missing keywords).
2. **`build_html`** — render the tailored sections through the Jinja2 template in `templates/html_template.html`.
3. **`build_pdf`** — print that HTML to A4 PDF with Playwright.
4. **`inspire_applicant`** / **`fry_applicant`** — Gen-Z pep talk for matched keywords, humorous roast for missing ones.

If a tool is called out of order, it tells the model which prerequisite to run first.

Tailoring rules (from the system prompt): keep existing sections, swap in the job’s wording for overlapping skills, rewrite the summary, and translate the CV to Spanish when the job description is in Spanish.

## Project layout

```
main.py                 Streamlit UI
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
    pdf_builder.py      Jinja2 HTML + Playwright PDF
templates/
  html_template.html    Resume layout
tests/                  Unit tests and a scripted agent walkthrough
evals/                  LangSmith dataset + LLM-as-judge evaluation
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

Create a `.env` in the project root (or one directory above it):

```env
GEMINI_API_KEY=your-key
MODEL_PRIMARY=gemini/gemini-2.5-flash
MODEL_BACKUP=gemini/gemini-2.0-flash
```

For LangSmith evaluations, also set `LANGSMITH_API_KEY`.

## Run the app

```bash
uv run streamlit run main.py
```

Paste a job description and click **Tailor CV**. The UI currently uses the sample CV in `tests/test_tailor_cv_node.py` (`BASE_CV`). You get:

- A downloadable `tailored_cv.pdf`
- An HTML preview of the resume
- **Fry Applicant** and **Inspire Applicant** commentary

## Call the agent directly

```python
from src.workflow_agent import compiled_agent

result = compiled_agent.invoke({
    "cv": open("my_cv.txt").read(),
    "job_description": open("job.txt").read(),
})

result["html_content"]   # styled HTML
result["pdf_bytes"]      # PDF bytes
result["keywords_matched"]
result["keywords_not_matched"]
result["inspiration"]
result["mock"]
```

## Tests

```bash
uv run pytest
```

`tests/verify_agent.py` walks the compiled graph with a scripted model (no live LLM, fake PDF) to check the happy path and the out-of-order tool guard.

## Evaluations

`evals/dataset.py` upserts examples into the LangSmith dataset `tailored_cv_dataset`. `evals/evaluator.py` runs the agent and scores tailored content against golden CVs with an LLM judge (`cv_alignment_score`).
