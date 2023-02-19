import os
import openai
import time
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd
from PyPDF2 import PdfReader
from decouple import config


''' Read file and transform Payload '''

files = list()
win = Tk()
icon = PhotoImage(file = r'logo.png')
win.iconphoto(False, icon)
win.title("NoteUp")

# Set the geometry of tkinter frame
win.geometry("700x350")

def open_file():
    global files
    file = fd.askopenfilenames(parent=win, title='Choose a File')
    tmp = win.splitlist(file)
    files.extend(tmp)
    print(files)
    for i in range(0,len(files)):
        Label(win,text=str(i+1)+'.').place(x=140,y=(i*50)+100)
        Label(win,text=files[i][files[i].rindex("/")+1::]).place(x=540,y=(i*50)+100)
    
def download():
    global files
    execute(files)
    win.destroy()

# Add a Label widget
l1 = Label(win, text="Select files to summarize", font=("BOLD",17), anchor=CENTER).place(x=250,y=10)
l2 = Label(win,text="SNo.",width=15,font=("BOLD",15),anchor=CENTER).place(x=70,y=50)
l3 = Label(win,text="LIST",width=30,font=("BOLD",15),anchor=CENTER).place(x=400,y=50)

# Add a Button Widget
b1=ttk.Button(win, text="Browse", command=open_file).place(x=110,y=300)
b2=ttk.Button(win, text="Download", state= NORMAL, command=download).place(x=540,y=300)


payload = ""
limit = 0

def execute(files):
    global payload
    for file_name in files:
        if file_name[len(file_name)-3::] =="txt":
            file_txt = open(file_name, "r")
            payload+=file_txt.read()
            file_txt.close()
        elif file_name[len(file_name)-3::] =="pdf":
            fileobj = open(file_name, "rb")
            file_pdf = PdfReader(fileobj).pages[0].extract_text()
            payload+=file_pdf

    ''' ChatGPT integration '''

    openai.api_key = config('API_KEY')
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="make brief notes in bullet points from the following.\n{}".format(payload),
      temperature=0.7,
      max_tokens=3000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    print(response)
    print(response['choices'][0]['text'])


    ''' Exporting output '''

    output_hack = open("C:\\Users\\Shruti\\AppData\\Local\\Programs\\Python\\Python311\\NoteUp\\output\\output{}.txt".format(time.time()), "a")
    output_hack.write(response['choices'][0]['text'])
    output_hack.close()

