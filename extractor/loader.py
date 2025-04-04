import pdfplumber

def read_pdf_pages(pdf_path):
    pdf = pdfplumber.open(pdf_path)
    return pdf.pages