from docling.document_converter import DocumentConverter
from io import BytesIO
from docling.datamodel.base_models import DocumentStream

class CVParser:
    def __init__(self):
        self.converter = DocumentConverter()

    def parse(self, cv_file: bytes) -> str:
        buf = BytesIO(cv_file)
        stream = DocumentStream(name="page.pdf", stream=buf)
        converted_file = self.converter.convert(stream)
        cv_string = converted_file.document.export_to_text
        return cv_string