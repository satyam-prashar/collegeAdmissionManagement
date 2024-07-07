from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk

class Form(Toplevel):
    def __init__(self,id):
        Toplevel.__init__(self)
        self.geometry("300x350")
        Tk.iconbitmap(self, default='images\icon_new.ico')
        self.title('Select Photo')

        frm = Frame(self)
        frm.pack(side=BOTTOM, padx=15, pady=15)

        lbl = Label(self)
        lbl.pack()

        btn = Button(frm, text="Browse Image", command=showimage)
        btn.pack(side=tk.LEFT)

        btn2 = btn = Button(frm, text="Exit", command=lambda: exit())
        btn2.pack(side=tk.LEFT, padx=15)

    def showimage():
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File",
                                         filetypes=(("JPG file", "*.jpg"), ("PNG file", "*.png"), ("All Files", "*.*")))
        img = Image.open(fln)
        img.thumbnail((350, 350))  # for resizing
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img)  # image
        lbl.image = img  # image
        print(fln)
