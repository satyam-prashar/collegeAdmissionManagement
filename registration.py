from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import datetime
date = datetime.datetime.now().date()
date = str(date)

# we can code without using self in right cases
con = sqlite3.connect('admission.db')
cur = con.cursor()
class Registration(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        LARGE_FONT = ("Posterama", 15)

        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))
        Tk.iconbitmap(self, default='images\icon_new.ico')
        self.state("zoomed")
        self.title('Registration')

        a = 0.3

        # frames
        self.right = Frame(self, height=0.7*self.winfo_screenheight(), width=0.5*self.winfo_screenwidth(),bg='#FFFFFF')
        self.right.place(x = 0.45*self.winfo_screenheight(),y = 0.05*self.winfo_screenwidth())

        self.label_name = Label(self.right, text="Registration", font=("Posterama", 30,'bold'), fg='#4361EE', bg='#FFFFFF')
        self.label_name.place(x = a*self.right.winfo_screenheight(),y = 0.01*self.right.winfo_screenwidth())

        self.entry_name = Entry(self.right, width=28, font=LARGE_FONT,  fg='#000000', bg='#FFFFFF')
        self.entry_name.insert(0, "Name")
        self.entry_name.place(x = a*self.right.winfo_screenheight(),y = 0.05*self.right.winfo_screenwidth())

        self.entry_password = Entry(self.right, width=28,  fg='#000000', bg='#FFFFFF', font=LARGE_FONT)
        self.entry_password.insert(0, "Password ")
        self.entry_password.place(x = a*self.right.winfo_screenheight(),y = 0.08*self.right.winfo_screenwidth())

        self.entry_Confirm_Password = Entry(self.right, width=28,  fg='#000000', bg='#FFFFFF', font=LARGE_FONT)
        self.entry_Confirm_Password.insert(0, "Confirm Password")
        self.entry_Confirm_Password.place(x = a*self.right.winfo_screenheight(),y = 0.11*self.right.winfo_screenwidth())

        self.entry_email = Entry(self.right, width=28,  fg='#000000', bg='#FFFFFF', font=LARGE_FONT)
        self.entry_email.insert(0, "Email")
        self.entry_email.place(x = a*self.right.winfo_screenheight(),y = 0.14*self.right.winfo_screenwidth())

        self.entry_phone = Entry(self.right, width=28,  fg='#000000', bg='#FFFFFF', font=LARGE_FONT)
        self.entry_phone.insert(0, "Phone Number")
        self.entry_phone.place(x = a*self.right.winfo_screenheight(),y = 0.17*self.right.winfo_screenwidth())

        self.entry_DOB = Entry(self.right, width=28,  fg='#000000', bg='#FFFFFF', font=LARGE_FONT)
        self.entry_DOB.insert(0, "DD/MM/YYYY")
        self.entry_DOB.place(x = a*self.right.winfo_screenheight(),y = 0.20*self.right.winfo_screenwidth())

        # info
        in_text ='After registering head to update registration to fill further information.'
        self.label_info = Label(self.right, text=in_text, font=("Posterama", 12), fg='#FFFFFF', bg='#4361EE')
        self.label_info.place(x = 0.2*self.right.winfo_screenheight(),y = 0.35*self.right.winfo_screenwidth())

        # button 1- Register
        button = Button(self.right, text="Register", font=("Posterama", 12,'bold'), width=10,  bg='#4361EE', fg='#FFFFFF', command=self.add_people)
        button.place(x = a*self.right.winfo_screenheight(),y = 0.25*self.right.winfo_screenwidth())
        # button 2- Cancel
        button = Button(self.right, text="Cancel", font=("Posterama", 12, 'bold'), width=10, bg='#4361EE',fg='#FFFFFF', command=self.destroy)
        button.place(x=0.53 * self.right.winfo_screenheight(), y=0.25 * self.right.winfo_screenwidth())


    def add_people(self):
        # name = self.entry_name.get()
        # Confirm_Password = self.entry_Confirm_Password.get()
        # email = self.entry_email.get()
        # DOB = self.entry_DOB.get()
        # phone = self.entry_phone.get()
        # password = self.entry_password.get()
        #
        # if name and Confirm_Password and email and phone and password !="":
        #     try:
        #         #add to database
        #         #inset into admission(perosn_id, person_name, Confirm_Password,etc)
        #         query ="insert into 'admission' (name, Confirm_Password, email, phone, password, DOB) values(?,?,?,?,?,?)"
        #         cur.execute(query, (name, Confirm_Password, email, phone, password,DOB))
        #         con.commit()
        #         messagebox.showinfo("Success","Contact Successful")
        #         self.destroy()
        #     except EXCEPTION as e:
        #         messagebox.showerror("Error", str(e))
        # else:
        #     messagebox.showerror("Error", "fill all the fields", icon='warning')
        pass