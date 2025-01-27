import pikepdf
from ebooklib import epub

def extract_text_from_file(file):
    # Determine file type and extract text accordingly
    if file.filename.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif file.filename.endswith(".epub"):
        return extract_text_from_epub(file)
    elif file.filename.endswith(".txt"):
        return file.file.read().decode("utf-8")
    else:
        raise ValueError("Unsupported file format")

# def extract_text_from_pdf(file):
#     reader = PyPDF2.PdfReader(file.file)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text()
#     return text



def extract_text_from_pdf(file):
    pdf = pikepdf.Pdf.open(file.file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

def extract_text_from_epub(file):
    book = epub.read_epub(file.file)
    text = ""
    for item in book.get_items():
        if item.get_type() == epub.ITEM_DOCUMENT:
            text += item.get_body_content().decode("utf-8")
    return text