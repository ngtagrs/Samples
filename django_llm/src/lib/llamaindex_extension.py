from llama_index.readers.file.docs import PDFReader
from llama_index.core.schema import Document
from pathlib import Path
import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader
from typing import Dict, List, Optional

class CustomPDFReader(PDFReader):
    """text pdf and image PDF parser"""
    def __init__(self):
        super().__init__()

    def load_data(self, file: Path, extra_info: Dict | None = None) -> List[Document]:
        if self.__is_image_pdf_file(file):
            return self.__extract_text_from_image_pdf(file)
        else:
            return super().load_data(file, extra_info)
            
    def __extract_text_from_image_pdf(self, pdf_path:Path, extra_info: Optional[Dict] = None) -> List[Document]:
        docs = []
        images = convert_from_path(pdf_path)
        for i, image in enumerate(images):
            page_text = pytesseract.image_to_string(image)
            metadata = {"page_label": i+1, "file_name": pdf_path.name}
            if extra_info is not None:
                metadata.update(extra_info)
            docs.append(Document(text=page_text, metadata=metadata))
        return docs
    
    def __is_image_pdf_file(self, file: Path) -> bool:
        with open(file, "rb") as pdf_file:
            reader = PdfReader(pdf_file)
            for page in  reader.pages:
                if len(page.extract_text())!=0:
                    return False
            return True