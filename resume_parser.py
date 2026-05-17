from PyPDF2 import PdfReader

def extract_text(pdf_file):

    text = ""

    reader = PdfReader(pdf_file)

    for page in reader.pages:
        text += page.extract_text()

    return text