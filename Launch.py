import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import PhotoImage
from urllib import request
import webbrowser
from data import happy, asmr, Relaxed, Bored
from random import randint


def Happy_playlist():
    x = randint(0, len(happy))
    #webbrowser.open(happy[x])
    text_label.config(state="normal")
    text_label.delete(1.0,END)
    text_label.insert(1.0,happy[x])
    text_label.config(state=DISABLED)


def Bored_playlist():
    x = randint(0, len(Bored))
    #webbrowser.open(Bored[x])
    text_label.config(state="normal")
    text_label.delete(1.0,END)
    text_label.insert(1.0,Bored[x])
    text_label.config(state=DISABLED)

def Relaxed_playlist():
    x = randint(0, len(Relaxed))
    #webbrowser.open(Relaxed[x])
    text_label.config(state="normal")
    text_label.delete(1.0,END)
    text_label.insert(1.0,Relaxed[x])
    text_label.config(state=DISABLED)



def Asmr_playlist():
    x = randint(0, len(asmr))
    #webbrowser.open(asmr[x])
    text_label.config(state="normal")
    text_label.delete(1.0,END)
    text_label.insert(1.0,asmr[x])
    text_label.config(state=DISABLED)

windows = tk.Tk()
frame = ttk.Frame(windows, padding=10)
x = ''
frame.grid()
text_label = tk.Text(
    frame,
    height=3,
    width=30,
    relief="solid",
    padx=10,
    pady=10,
    wrap=tk.WORD
)
text_label.grid(pady=20,column=3,row=4)  # Add some vertical spacing

Bored_button = tk.Button(frame, text="Bored", command=Bored_playlist)
Bored_button.grid(
    column=0, row=0)
    

Relaxed_button = tk.Button(frame, text="Relaxed", command=Relaxed_playlist)
Relaxed_button.grid(
    column=2, row=0)
Happy_button = tk.Button(frame, text="Happy", command=Happy_playlist)
Happy_button.grid(
    column=3, row=0)
Asmr_button = tk.Button(
    frame, text="Asmr", command=Asmr_playlist)
Asmr_button.grid(column=1, row=0)

Label = tk.Label(frame, text=x)
Label.grid(column=2, row=2)
Label.grid()
windows.mainloop()




def test(x):
    y = "hmmm"
    return y



