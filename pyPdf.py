<<<<<<< HEAD
"""
#Read from PDF

from pypdf import PdfReader
 
reader = PdfReader("Intern.pdf")
=======
#Read from PDF

from pypdf import PdfReader

reader = PdfReader("Sample.pdf")
>>>>>>> 46f29625bb7b97eb356132268cfa07f280a62e7f

print("Number of pages:", len(reader.pages))

for page in reader.pages:
    text = page.extract_text()
    print(text)


#Copy Paste from exisiting PDF
<<<<<<< HEAD

from pypdf import PdfReader, PdfWriter

reader = PdfReader("Intern.pdf")
=======
"""
from pypdf import PdfReader, PdfWriter

reader = PdfReader("sample.pdf")
>>>>>>> 46f29625bb7b97eb356132268cfa07f280a62e7f
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

with open("output.pdf", "wb") as f:
    writer.write(f)
<<<<<<< HEAD

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
=======
    """


#Merge PDFs
"""
from pypdf import PdfWriter

writer = PdfWriter()

writer.append("input-1.pdf")
writer.append("input-2.pdf")

writer.write("merged.pdf")
writer.close()
"""
>>>>>>> 46f29625bb7b97eb356132268cfa07f280a62e7f
