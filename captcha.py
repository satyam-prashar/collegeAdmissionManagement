from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import datetime
import random
date = datetime.datetime.now().date()
date = str(date)

class Captcha(Toplevel):
    def __init__(self,*args, **kwargs):
        Toplevel.__init__(self,*args, **kwargs)
        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))
        Tk.iconbitmap(self, default='images\icon_new.ico')
        self.state("zoomed")
        self.title('Captcha')

        self.captcha1 = PhotoImage(file="images\capt\cap1.png")
        self.captcha2 = PhotoImage(file="images\capt\cap2.png")
        self.captcha3 = PhotoImage(file="images\capt\cap3.png")
        self.captcha4 = PhotoImage(file="images\capt\cap4.png")
        self.captcha5 = PhotoImage(file="images\capt\cap5.png")
        self.captcha6 = PhotoImage(file="images\capt\cap6.png")
        self.captcha7 = PhotoImage(file="images\capt\cap7.png")
        self.captcha8 = PhotoImage(file="images\capt\cap8.png")
        self.captcha9 = PhotoImage(file="images\capt\cap9.png")
        arr = [self.captcha1, self.captcha2, self.captcha3, self.captcha4, self.captcha5, self.captcha6, self.captcha7, self.captcha8, self.captcha9]
        self.pic_no = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8 ])

        p1 = self.repeat()

    def submit(self):
        user_ans = self.entry_captcha.get()
        ans = ['CY6V', '38WE', 'TER3N', 'NPT5', 'S694', 'XKBW', 'WD54J', 'HU68','w34a5']
        if user_ans==ans[self.pic_no]:
            print("Success")
        else:
            messagebox.showinfo("Info", "Wrong Captcha")

    def repeat(self):
        arr = [self.captcha1, self.captcha2, self.captcha3, self.captcha4, self.captcha5, self.captcha6, self.captcha7,
               self.captcha8, self.captcha9]

        self.left = Frame(self, height=0.75 * self.winfo_screenheight(), width=0.55 * self.winfo_screenwidth(), bg='#FFFFFF')
        self.left.place(x=0.25 * self.winfo_screenwidth(), y=0.1 * self.winfo_screenheight())

        self.pic_no = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])

        top_image_label2 = Label(self.left, image=arr[self.pic_no])
        top_image_label2.place(x=0.2 * self.left.winfo_screenwidth(), y=0.15 * self.left.winfo_screenwidth())

        self.entry_captcha = ttk.Entry(self.left, width=25, font=("Posterama", 20))
        self.entry_captcha.insert(0, "Enter Captcha", )
        self.entry_captcha.focus()
        self.entry_captcha.place(x=0.2 * self.left.winfo_screenwidth(), y=0.35 * self.left.winfo_screenheight())

        self.new_admission = Button(self.left, width=22, text="Login", fg='#4361EE',
                                    font=("Posterama", 20, 'bold'), bg='#FFFFFF', command=self.submit)
        self.new_admission.place(x=0.025 * self.left.winfo_screenwidth(), y=0.6 * self.left.winfo_screenheight())

        self.refresh = Button(self.left, width=8, text="Refresh", fg='#4361EE', font=("Posterama", 12, 'bold'),
                              bg='#FFFFFF', command=self.repeat)
        self.refresh.place(x=0.025 * self.left.winfo_screenwidth(), y=0.45 * self.left.winfo_screenheight())


