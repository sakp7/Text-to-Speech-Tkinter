import tkinter as tk
from tkinter import *
import pyttsx3


ts=tk.Tk()
ts.title("Text to Speech App")
ts.geometry("500x300")
ts.resizable(False,False)

#creating text to speech engine using pyttsx3

engine=pyttsx3.init()
def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()


textv=StringVar()
obj=LabelFrame(ts,text="Text to speech",font=20,bd=1)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

lbl=Label(obj,text="Text",font=30)
lbl.pack(side="left",padx=5)


text=Entry(obj,textvariable=textv,font=30,width=25,bd=5)
text.pack(side="left",padx=10)

b=Button(obj,text="Speech",font=20,bg="black",fg="white",command=speaknow)
b.pack(side="left",padx=10)


ts.mainloop()