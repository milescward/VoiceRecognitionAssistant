import speech_recognition as sr
from tkinter import *
from tkinter.scrolledtext import *



 
root = Tk()
e = ScrolledText(root, relief=GROOVE, height=15, width=60, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
r = sr.Recognizer()

def record():
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        response = r.recognize_google(audio)
        e.insert(END, response)
    except sr.UnknownValueError:
        return "error"


def copy():
    root.clipboard_clear
    root.clipboard_append(str(e.get(1.0, END)))
    e.delete(1.0, END)


root.title("Voice Assistant")
copy_button = Button(root, relief=GROOVE, text="Copy", padx=5, pady=5, command=copy)
recordButton = Button(root, relief=GROOVE, text="Start recording", padx=5, pady=5, command=record)
e.grid(row=1, column=0)
recordButton.grid(row=2, column=1)
copy_button.grid(row=2, column=2)

root.mainloop()