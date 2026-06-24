"""
#Read from PDF

from pypdf import PdfReader
 
reader = PdfReader("Intern.pdf")

print("Number of pages:", len(reader.pages))

for page in reader.pages:
    text = page.extract_text()
    print(text)


#Copy Paste from exisiting PDF

from pypdf import PdfReader, PdfWriter

reader = PdfReader("Intern.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

with open("output.pdf", "wb") as f:
    writer.write(f)

#Merge PDFs
from pypdf import PdfWriter
writer = PdfWriter()
writer.append("Intern.pdf")
writer.append("Samplemaam.pdf.pdf")

writer.write("Merged.pdf")
writer.close()
"""

from pypdf import PdfReader, PdfWriter
writer1 = PdfWriter()  
reader = PdfReader("Intern.pdf")
