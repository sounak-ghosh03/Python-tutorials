# Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. 
# You are welcome to add more functionalities


from PyPDF2 import PdfReader, PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir("C:\\Users\\souna\\Desktop\\certificates") if file.endswith(".pdf")]         

    #In Python strings, the backslash (\) is an escape character. This means Python treats the \ as a special character followed by a command.
    #When specifying paths in Python, we should use either double backslashes (\\) or raw strings(r)

for pdf in files:
    pdf_file_path = os.path.join("C:\\Users\\souna\\Desktop\\certificates", pdf)
    with open(pdf_file_path, "rb") as fileobj:
        pdf_reader = PdfReader(fileobj)
        for page in pdf_reader.pages:
            merger.add_page(page)

with open("merged-pdf.pdf", "wb") as output_pdf:
    merger.write(output_pdf)
