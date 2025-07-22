import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader
from docx import Document

def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_url(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    for script in soup(["script", "style"]):
        script.extract()
    return soup.get_text()

def extract_text_from_docx(file_path: str) -> str:
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])
