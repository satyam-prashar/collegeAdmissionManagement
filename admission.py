from tkinter import *

from tkinter import messagebox
from tkinter import ttk
import sqlite3
from form import Form
from about_us import About_Us
from fees_structure import Fees_Structure
import datetime
import sqlite3
from tkinter import messagebox
# we can code without using self in bottom cases
con = sqlite3.connect('student_info.db')
cur = con.cursor()

date = datetime.datetime.now().date()
date = str(date)

class Admission(Toplevel):
    def __init__(self,id):
        Toplevel.__init__(self)
        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))
        Tk.iconbitmap(self, default='images\icon_new.ico')
        self.state("zoomed")
        self.title('Admission')
        self.id = id

        # background image
        self.top_image = PhotoImage(file="images/college2.png")
        self.top_image_label = Label(self, image=self.top_image, bg="#FFFFFF")
        self.top_image_label.place(x=-5, y=-5)

        set = 0
        # frames
        self.left = Frame(self, height=0.75 * self.winfo_screenheight(), width=0.55 * self.winfo_screenwidth(),bg='#FFFFFF')
        self.left.place(x=0.06 * self.winfo_screenwidth(), y=0.1 * self.winfo_screenheight())

        self.right = Frame(self, height=0.75 * self.winfo_screenheight(), width=0.3 * self.winfo_screenwidth(),bg='#B5179E')
        self.right.place(x=0.6 * self.winfo_screenwidth(), y=0.1 * self.winfo_screenheight())

        query = "select * from student where id ='{}'".format(id)
        result = cur.execute(query).fetchone()

        self.pro = result[32]
        # LEFT Frame
        self.welcome_id = Label(self.left, text="Welcome, "+ result[2], fg='#B5179E',font=("Posterama", 30, 'bold'), bg='#FFFFFF')
        self.welcome_id.place(x=0.15 * self.left.winfo_screenwidth(), y=0.05 * self.left.winfo_screenheight())

        req_text = " "
        if result[4] == "Father Name":
            req_text ="Please, Proceed to Fill the form"
        elif result[22] == "Marks (%age)":
            req_text = "Please, Complete the Form"
        else:
            req_text = "Please, Make sure you have uploaded all your Documents"

        #condition application
        self.welcome_id = Label(self.left, text=req_text, fg='#B5179E', font=("Posterama", 20, ), bg='#FFFFFF')
        self.welcome_id.place(x=0.05 * self.left.winfo_screenwidth(), y=0.25 * self.left.winfo_screenheight())


        if result[33]== "Pending":
            req_text2  =" Your Application is under processing, \n Please Check out after some day for Update"
        elif result[33]== "Selected":
            req_text2  =" Your Application is SELECTED,Congratulations!!!\n We welcome you to your New Journey\n Click On JOIN to Start the Journey"
            set = 1
        else:
            req_text2  = " Your Application is REJECTED, \nWe are extremly sorry about it."
        self.welcome_id = Label(self.left, text=req_text2, fg='#FFFFFF', font=("Posterama", 20, 'bold'),
                                bg='#B5179E')
        self.welcome_id.place(x=0.05 * self.left.winfo_screenwidth(), y=0.60 * self.left.winfo_screenheight())

        # Right Frame

        self.form = Button(self.right, width=22, text="Fill Form", fg='#B5179E', font=("Posterama", 20, 'bold'), bg='#FFFFFF', command=self.formfill)
        self.form.place(x=0.025 * self.right.winfo_screenwidth(), y=0.2 * self.right.winfo_screenheight())

        self.fees = Button(self.right, width=22, text="Fees Structure", fg='#B5179E',font=("Posterama", 20, 'bold'), bg='#FFFFFF', command=self.fees)
        self.fees.place(x=0.025 * self.right.winfo_screenwidth(), y=0.3 * self.right.winfo_screenheight())

        self.about_us = Button(self.right, width=22, text="About Us", fg='#B5179E',font=("Posterama", 20, 'bold'), bg='#FFFFFF', command=self.about)
        self.about_us.place(x=0.025 * self.right.winfo_screenwidth(), y=0.4 * self.right.winfo_screenheight())

        self.Exit = Button(self.right, width=22, text="Exit", fg='#B5179E', font=("Posterama", 20, 'bold'),
                               bg='#FFFFFF', command=self.destroy)
        self.Exit.place(x=0.025 * self.right.winfo_screenwidth(), y=0.5 * self.right.winfo_screenheight())

        if set == 1:
            self.classs = Button(self.right, width=22, text="JOIN!!!!!", fg='#B5179E', font=("Posterama", 20, 'bold'),
                           bg='#FFFFFF', command=self.class_join)
            self.classs.place(x=0.025 * self.right.winfo_screenwidth(), y=0.65 * self.right.winfo_screenheight())


    def fees(self):
        display = Fees_Structure()

    def formfill(self):
        display = Form(self.id)

    def about(self):
        display = About_Us()

    def class_join(self):
        query ="update student set class = '{}' where id = {}".format("member",self.id)
        cur.execute(query)
        con.commit()
        query = "insert into dashboard (id,program,section,rollno,attendence) values(?,?,?,?,?)"
        cur.execute(query,(self.id,self.pro,"K18TM","76","45"))
        con.commit()

        messagebox.showinfo("Success", "Please Login Again to Start")
        self.destroy()
