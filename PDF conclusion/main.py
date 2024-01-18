from chatsimple import chat_with_gpt3
import pypdfium2 
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

prompt = ""
pdf = pypdfium2.PdfDocument(filename)
for i in range(len(pdf)):
    page = pdf.get_page(i)
    textpage = page.get_textpage()
    prompt += textpage.get_text_range() + "\n"
    [g.close() for g in (textpage, page)]
pdf.close()
print(prompt)
print(chat_with_gpt3(prompt))