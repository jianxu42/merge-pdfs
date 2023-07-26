import base64

import PyPDF2
from flask import Flask, request

app = Flask(__name__)


@app.route('/merge_pdfs', methods=['POST'])
def merge_pdfs():
    data = request.get_json()

    base64_content1 = data.get('file1')
    base64_content2 = data.get('file2')
    pdf_bytes1 = base64.b64decode(base64_content1)
    pdf_bytes2 = base64.b64decode(base64_content2)
    with open("file1.pdf", "wb") as file:
        file.write(pdf_bytes1)
    with open("file2.pdf", "wb") as file:
        file.write(pdf_bytes2)

    # Open the first PDF file
    pdf1 = open('file1.pdf', 'rb')
    pdf1_reader = PyPDF2.PdfReader(pdf1)

    # Open the second PDF file
    pdf2 = open('file2.pdf', 'rb')
    pdf2_reader = PyPDF2.PdfReader(pdf2)

    # Create a new PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Add the pages of the first PDF file to the writer object
    for page_num in range(len(pdf1_reader.pages)):
        page = pdf1_reader.pages[page_num]
        pdf_writer.add_page(page)

    # Add the pages of the second PDF file to the writer object
    for page_num in range(len(pdf2_reader.pages)):
        page = pdf2_reader.pages[page_num]
        pdf_writer.add_page(page)

    # Write the merged PDF file to disk
    pdf_output = open('merged.pdf', 'wb')
    pdf_writer.write(pdf_output)

    # Close the input and output files
    pdf1.close()
    pdf2.close()
    pdf_output.close()

    # Open the PDF file
    with open('merged.pdf', 'rb') as f:
        pdf_bytes = f.read()
        base64_string = base64.b64encode(pdf_bytes).decode('utf-8')

    return base64_string
