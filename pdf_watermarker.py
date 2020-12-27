import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

with open(sys.argv[2], 'rb') as import_file, open(sys.argv[1], 'rb') as watermark_file:
    document, watermark = PdfFileReader(import_file), PdfFileReader(watermark_file)
    watermark_page = watermark.getPage(0)
    ready_file = PdfFileWriter()

    for i in range(document.getNumPages()):
        pdf_page = document.getPage(i)
        pdf_page.mergePage(watermark_page)
        ready_file.addPage(pdf_page)

    document_with_watermark = './document_with_watermark.pdf'
    with open(document_with_watermark, "wb") as solution:
        ready_file.write(solution)