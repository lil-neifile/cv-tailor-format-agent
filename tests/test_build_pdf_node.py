from pathlib import Path

from src.graph.nodes import build_PDF, build_html
from tests.test_format_tailored_content_node import TAILORED_CONTENT

OUTPUT_PDF = Path(__file__).parent / "output.pdf"


def test_build_pdf_node_outputs_results():
    html_content = build_html(
        {"tailored_content": TAILORED_CONTENT}
    )["html_content"]
    result = build_PDF({"html_content": html_content})
    OUTPUT_PDF.write_bytes(result["pdf_bytes"])
    print(OUTPUT_PDF)
