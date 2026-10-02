from jinja2 import Environment, FileSystemLoader, select_autoescape

from config import config


class HTMLBuilder:
    def __init__(self):
        self.env = Environment(
            loader=FileSystemLoader(config.TEMPLATES_DIR),
            autoescape=select_autoescape(["html"]),
        )

    def build_html(self, **TailoredContent) -> str:
        template = self.env.get_template(config.TEMPLATE_NAME)
        return template.render(**TailoredContent)

    def build_pdf(self, html: str) -> bytes:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            try:
                page = browser.new_page()
                page.set_content(html, wait_until="networkidle")
                return page.pdf(format="A4", print_background=True)
            finally:
                browser.close()
