<<<<<<< HEAD
#from pypdf import PdfReader
#reader = PdfReader("Intern.pdf")
#print("Number of pages:", len(reader.pages))    
#for i in range(len(reader.pages)):
#    page = reader.pages[i].extract_text()
#    print(page)
#for i in page.images():
#    with open(i.name, "wb") as f:   
#        f.write(i.data)
#full_text = ""
#for i, page in enumerate(reader.pages, start=1):
#    full_text += f"\n--- Page {i} ---\n" + page.extract_text()
#print(full_text)

              ##python lists
#playlist = ["Shape of you", "Blinding Lights", "Levitating",]
#print("The current playing song is:",playlist[0])
#print("Enter the song you want to play next:")
#next_song = playlist.append(input())
#print("The song",playlist[-1],"is added to the queue")
#print(playlist)

=======
# from pypdf import PdfReader
# reader = PdfReader("sample.pdf")
# pages = len(reader.pages)
# print(pages)
# page = reader.pages[0]

# for i in range(pages):
#     page = reader.pages[i]
#     print(page.extract_text())-------------------------------------------------------------------

import langchain

print(langchain.__version__)
>>>>>>> 46f29625bb7b97eb356132268cfa07f280a62e7f
