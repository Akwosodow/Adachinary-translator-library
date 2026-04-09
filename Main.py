from tkinter import *
from tkinter import ttk
import Adachinary as Ad


root = Tk()
root.geometry("550x230")
root.title("Adachinary Translator")
frm = ttk.Frame(root, padding=13)
frm.grid()

def test() -> None:
    outputbox.delete(1.0, END)
    outputbox.insert(END, input.get())

def adachitranslate() -> None:
    outputbox.delete(1.0, END)
    outputbox.insert(END, Ad.TheOtherWay(input.get()))

def binary(adachiflag: bool) -> None:
    outputbox.delete(1.0, END)
    if adachiflag == True:
        outputbox.insert(END, Ad.Adachit(Ad.Binary(input.get())))
    else:
        outputbox.insert(END, Ad.Binary(input.get()))

def morse(adachiflag: bool) -> None:
    outputbox.delete(1.0, END)
    if adachiflag == True:
        outputbox.insert(END, Ad.Adachit(Ad.Morse(input.get())))
    else:
        outputbox.insert(END, Ad.Morse(input.get()))

input = StringVar()

ttk.Label(frm, text="Input:").grid(column=0, row=0)
ttk.Entry(frm, textvariable = input).grid(column=1, row=0)

ttk.Label(frm, text="Output:").grid(column=0, row=1)
outputbox = Text(frm, height = 3, width = 50)
outputbox.grid(column=1, row=1)

ttk.Label(frm, text="Adaching Options:").grid(column=0,row=2)
ttk.Label(frm, text="Lame Options:").grid(column=1,row=2)

ttk.Button(frm, text = "Adachinary", command = lambda: binary(1)).grid(column=0, row=3)
ttk.Button(frm, text = "Morsedachi", command = lambda: morse(1)).grid(column=0, row=4)
ttk.Button(frm, text = "Undachi", command = adachitranslate).grid(column=0, row=5) 
ttk.Button(frm, text = "Binary", command = lambda: binary(0)).grid(column=1, row=3)
ttk.Button(frm, text = "Morse", command = lambda: morse(0)).grid(column=1, row=4)

root.mainloop()
