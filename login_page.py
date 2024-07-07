from tkinter import *
from tkinter import ttk
from student_homepage import Student_Homepage
#from registration import Registration
from admission import Admission
from admin import Admin
from captcha import Captcha
from form import Form
from fees_structure import Fees_Structure
from about_us import About_Us
from student_homepage import Student_Homepage
import random
import datetime
from PIL import Image, ImageTk

import sqlite3
from tkinter import messagebox
# we can code without using self in bottom cases
con = sqlite3.connect('student_info.db')
cur = con.cursor()

date = datetime.datetime.now().date()
date = str(date)
time = datetime.datetime.now().time()
time = str(time)
time = time.split(":")

LARGE_FONT=("Posterama",12)

class Application(object):
    def __init__(self, master):
        self.master = master

        # background image
        self.top_image = PhotoImage(file="images/About_us college.png")
        self.top_image_label = Label(master, image=self.top_image,bg="#FFFFFF")
        self.top_image_label.place(x=-5, y=-5)

        # frames
        self.left = Frame(master, height = 0.75*master.winfo_screenheight(), width =0.55*master.winfo_screenwidth(), bg='#FFFFFF')
        self.left.place(x=0.06*master.winfo_screenwidth(),y=0.1*master.winfo_screenheight())

        self.right = Frame(master,height = 0.75*master.winfo_screenheight(), width =0.3*master.winfo_screenwidth(), bg = '#4361EE' )
        self.right.place(x= 0.6*master.winfo_screenwidth(),y=0.1*master.winfo_screenheight())

        #RIGHT FRAME
        #date
        self.date_lbl = Label(self.right, text="Date- "+date, font=("Posterama", 12,'bold'), bg='#4361EE', fg='#FFFFFF')
        self.date_lbl.place(x=0.2* self.right.winfo_screenwidth(), y=0.01 * self.right.winfo_screenheight())
        self.time_lbl = Label(self.right, text="Time- " + time[0] +":"+ time[1], font=("Posterama", 12,'bold'), bg='#4361EE', fg='#FFFFFF')
        self.time_lbl.place(x=0.2 * self.right.winfo_screenwidth(), y=0.04 * self.right.winfo_screenheight())

        #text
        self.label_id = Label(self.right, text="Login ", font=("Posterama",45, 'bold'), bg = '#4361EE', fg='#FFFFFF')
        self.label_id.place(x= 0.025*self.right.winfo_screenwidth(), y= 0.2*self.right.winfo_screenheight())

        #entry Box
        aInteger = IntVar()

        def activateCheck():
            if aInteger.get() == 1:  # whenever checked
                self.entry_password.config(show="")
            elif aInteger.get() == 0:  # whenever unchecked
                self.entry_password.config(show="*")
        self.chk = Checkbutton(self.right, variable=aInteger, command=activateCheck, bg='#4361EE')
        self.chk.place(x=0.025 * self.right.winfo_screenwidth(),
                       y=0.425 * self.right.winfo_screenheight())
        self.label_id = Label(self.right, text="Show Password", font=("Posterama", 10, 'bold'), bg='#4361EE', fg='#FFFFFF')
        self.label_id.place(x=0.035 * self.right.winfo_screenwidth(),
                       y=0.425 * self.right.winfo_screenheight())

        ########        USERNAME                ##########
        self.entry_id = ttk.Entry(self.right, width=25, font=("Posterama",20))
        self.entry_id.insert(0, "Username",)
        self.entry_id.focus()
        self.entry_id.place(x= 0.025*self.right.winfo_screenwidth(), y= 0.32*self.right.winfo_screenheight())
        ############ Password #######################
        self.entry_password = ttk.Entry(self.right, width=25, font=("Posterama",20))
        self.entry_password.insert(0, "Password")
        self.entry_password.config(show="*")
        self.entry_password.place(x= 0.025*self.right.winfo_screenwidth(), y= 0.38*self.right.winfo_screenheight())

        #button
        self.login = Button(self.right, width=8, text="Login", fg='#4361EE', font=("Posterama",12, 'bold'), bg='#FFFFFF', command=self.login)
        self.login.place(x= 0.025*self.right.winfo_screenwidth(), y= 0.46*self.right.winfo_screenheight())

        self.exit = Button(self.right, width=8, text="Exit", fg='#4361EE', font=("Posterama", 12, 'bold'),bg='#FFFFFF', command=master.destroy)
        self.exit.place(x=0.215 * self.right.winfo_screenwidth(), y=0.46 * self.right.winfo_screenheight())


        #new admission

        self.new_admission = Button(self.right, width=22, text="New Admission", fg='#4361EE',font=("Posterama", 20, 'bold'), bg='#FFFFFF', command=self.admission)
        self.new_admission.place(x=0.025 * self.right.winfo_screenwidth(), y=0.6 * self.right.winfo_screenheight())

        # text
        self.label_id = Label(self.right, text="OR ", font=("Posterama", 12), bg='#4361EE', fg='#FFFFFF')
        self.label_id.place(x=0.135 * self.right.winfo_screenwidth(), y=0.55 * self.right.winfo_screenheight())

     #####   #LEFT FRAME
        # text
        # self.welcome_id = Label(self.left, text="Welcome TO  ", font=("Papyrus", 45), bg='#FFFFFF', fg='#023E8A')
        # self.welcome_id.place(x=0.15*self.left.winfo_screenwidth(), y= 0.05*self.left.winfo_screenheight())

        #image
        self.logo_image = PhotoImage(file="images/logo (1).png")
        self.logo_image_label = Label(self.left, image=self.logo_image)
        self.logo_image_label.place(x=0.1*self.left.winfo_screenwidth(), y= 0.08*self.left.winfo_screenheight())

        # text
        # self.welcome_id = Label(self.left, text="ALDRIDGE COLLEGE UNIVERSITY ", font=("Univers", 30,), bg='#FFFFFF', fg='#023E8A')
        # self.welcome_id.place(x=0.055 * self.left.winfo_screenwidth(), y=0.5 * self.left.winfo_screenheight())

    def login(self):
        name = self.entry_id.get()
        password = self.entry_password.get()
        if password == 'password' and name == 'admin':
            display_2 = Admin()
        else:
            try:
                query = "select * from student where email ='{}'".format(name)
                result = cur.execute(query).fetchone()
                id = result[0]
                cl = result[1]
                password_check = result[29]
                if password == password_check:
                    if cl == "application":
                        display_3 = Admission(id)
                    else:
                        display_3 = Student_Homepage(id)
                else:
                    messagebox.showinfo("Info", "wrong password")
            except Exception as e:
                messagebox.showinfo("Info", "Wrong User ID")
                print(str(e))

    def admission(self):
        self.captcha1 = PhotoImage(file="images\capt\cap1.png")
        self.captcha2 = PhotoImage(file="images\capt\cap2.png")
        self.captcha3 = PhotoImage(file="images\capt\cap3.png")
        self.captcha4 = PhotoImage(file="images\capt\cap4.png")
        self.captcha5 = PhotoImage(file="images\capt\cap5.png")
        self.captcha6 = PhotoImage(file="images\capt\cap6.png")
        self.captcha7 = PhotoImage(file="images\capt\cap7.png")
        self.captcha8 = PhotoImage(file="images\capt\cap8.png")
        self.captcha9 = PhotoImage(file="images\capt\cap9.png")
        self.captcha10 = PhotoImage(file="images\capt\cap10.png")
        self.captcha11 = PhotoImage(file="images\capt\cap11.png")
        self.captcha12 = PhotoImage(file="images\capt\cap12.png")
        self.captcha13 = PhotoImage(file="images\capt\cap13.png")
        self.captcha14 = PhotoImage(file="images\capt\cap14.png")
        self.captcha15 = PhotoImage(file="images\capt\cap15.png")

        p1 = self.repeat()

    def repeat(self):

        self.arr = [self.captcha1, self.captcha2, self.captcha3, self.captcha4, self.captcha5, self.captcha6,self.captcha7,
                    self.captcha8, self.captcha9]
        self.pic_no = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15])

        self.right = Frame(self.master, height=0.75 * self.master.winfo_screenheight(), width=0.3 * self.master.winfo_screenwidth(),
                           bg='#4361EE')
        self.right.place(x=0.6 * self.master.winfo_screenwidth(), y=0.1 * self.master.winfo_screenheight())

        self.date_lbl = Label(self.right, text="Date- " + date, font=("Posterama", 12, 'bold'), bg='#4361EE',
                              fg='#FFFFFF')
        self.date_lbl.place(x=0.2 * self.right.winfo_screenwidth(), y=0.01 * self.right.winfo_screenheight())
        self.time_lbl = Label(self.right, text="Time- " + time[0] + ":" + time[1], font=("Posterama", 12, 'bold'),
                              bg='#4361EE', fg='#FFFFFF')
        self.time_lbl.place(x=0.2 * self.right.winfo_screenwidth(), y=0.04 * self.right.winfo_screenheight())

        # text
        self.label_id = Label(self.right, text="Captcha ", font=("Posterama", 45, 'bold'), bg='#4361EE', fg='#FFFFFF')
        self.label_id.place(x=0.025 * self.right.winfo_screenwidth(), y=0.2 * self.right.winfo_screenheight())

        # entry Box
        self.entry_id = Label(self.right, image=self.arr[self.pic_no])
        self.entry_id.place(x=0.025 * self.right.winfo_screenwidth(), y=0.32 * self.right.winfo_screenheight())

        self.entry_captcha = ttk.Entry(self.right, width=25, font=("Posterama", 20))
        self.entry_captcha.insert(0, "Please Enter the Captcha")
        self.entry_captcha.place(x=0.025 * self.right.winfo_screenwidth(), y=0.40 * self.right.winfo_screenheight())

        self.refresh = Button(self.right, width=8, text="Refresh", fg='#4361EE', font=("Posterama", 12, 'bold'), bg='#FFFFFF', command=self.repeat)
        self.refresh.place(x=0.215 * self.right.winfo_screenwidth(), y=0.32 * self.right.winfo_screenheight())

        self.confirm = Button(self.right, width=22, text="Confirm", fg='#4361EE', font=("Posterama", 20, 'bold'),
                            bg='#FFFFFF', command=self.submit)
        self.confirm.place(x=0.025 * self.right.winfo_screenwidth(), y=0.45 * self.right.winfo_screenheight())

        self.back = Button(self.right, width=8, text="Back", fg='#4361EE',
                                    font=("Posterama", 12, 'bold'), bg='#FFFFFF', command=self.right.destroy)
        self.back.place(x=0.025 * self.right.winfo_screenwidth(), y=0.6 * self.right.winfo_screenheight())

    def submit(self):
        user_ans = self.entry_captcha.get()
        ans = ['CY6V', '38WE', 'TER3N', 'NPT5', 'S694', 'XKBW', 'WD54J', 'HU68', 'W34a5']
        if user_ans == ans[self.pic_no]:
            p1 = self.registration()
        else:
            messagebox.showinfo("Info", "Wrong Captcha")

    def registration(self):
        self.right = Frame(self.master, height=0.75 * self.master.winfo_screenheight(),width=0.3 * self.master.winfo_screenwidth(), bg='#4361EE')
        self.right.place(x=0.6 * self.master.winfo_screenwidth(), y=0.1 * self.master.winfo_screenheight())

        self.date_lbl = Label(self.right, text="Date- " + date, font=("Posterama", 12, 'bold'), bg='#4361EE',fg='#FFFFFF')
        self.date_lbl.place(x=0.2 * self.right.winfo_screenwidth(), y=0.01 * self.right.winfo_screenheight())
        self.time_lbl = Label(self.right, text="Time- " + time[0] + ":" + time[1], font=("Posterama", 12, 'bold'), bg='#4361EE', fg='#FFFFFF')
        self.time_lbl.place(x=0.2 * self.right.winfo_screenwidth(), y=0.04 * self.right.winfo_screenheight())

        # text
        self.label_id = Label(self.right, text="Registration ", font=("Posterama", 45, 'bold'), bg='#4361EE', fg='#FFFFFF')
        self.label_id.place(x=0.025 * self.right.winfo_screenwidth(), y=0.08 * self.right.winfo_screenheight()+10)

        self.label_id = Label(self.right, text="Email ID ", font=("Posterama", 14, 'bold'), bg='#4361EE',fg='#FFFFFF')
        self.label_id.place(x=0.025 * self.right.winfo_screenwidth(), y=0.175 * self.right.winfo_screenheight()+15)

        self.email_id = ttk.Entry(self.right, width=25, font=("Posterama", 20))
      #  self.email_id.insert(0, "Email ID", )
        self.email_id.focus()
        self.email_id.place(x=0.025 * self.right.winfo_screenwidth(), y=0.2 * self.right.winfo_screenheight()+15)

        self.label_id = Label(self.right, text="Enter Password", font=("Posterama", 14, 'bold'), bg='#4361EE', fg='#FFFFFF')
        self.label_id.place(x=0.025 * self.right.winfo_screenwidth(), y=0.255 * self.right.winfo_screenheight()+15)

        aInteger = IntVar()
        def activateCheck():
            if aInteger.get() == 1:  # whenever checked
                self.entry_password.config(show="")
                self.confirm_password.config(show="")
            elif aInteger.get() == 0:  # whenever unchecked
                self.entry_password.config(show="*")
                self.confirm_password.config(show="*")
        self.chk = Checkbutton(self.right, variable=aInteger, command=activateCheck, bg='#4361EE')
        self.chk.place(x=0.025 * self.right.winfo_screenwidth(),
                       y=0.425 * self.right.winfo_screenheight())
        self.label_id = Label(self.right, text="Show Password", font=("Posterama", 10, 'bold'), bg='#4361EE', fg='#FFFFFF')
        self.label_id.place(x=0.035 * self.right.winfo_screenwidth(), y=0.425 * self.right.winfo_screenheight())

        self.entry_password = ttk.Entry(self.right, width=25, font=("Posterama", 20))
       # self.entry_password.insert(0, "Enter Password")
        self.entry_password.config(show="*")
        self.entry_password.place(x=0.025 * self.right.winfo_screenwidth(), y=0.28 * self.right.winfo_screenheight()+15)

        self.label_id = Label(self.right, text="Confirm Password", font=("Posterama", 14, 'bold'), bg='#4361EE',fg='#FFFFFF')
        self.label_id.place(x=0.025 * self.right.winfo_screenwidth(), y=0.335 * self.right.winfo_screenheight()+15)

        self.confirm_password = ttk.Entry(self.right, width=25, font=("Posterama", 20))
        #self.confirm_password.insert(0, "Confirm Password")
        self.confirm_password.config(show="*")
        self.confirm_password.place(x=0.025 * self.right.winfo_screenwidth(), y=0.36 * self.right.winfo_screenheight()+15)

        self.label_id = Label(self.right, text="Phone Number", font=("Posterama", 14, 'bold'), bg='#4361EE', fg='#FFFFFF')
        self.label_id.place(x=0.025 * self.right.winfo_screenwidth(), y=0.415 * self.right.winfo_screenheight()+28)

        self.phone = ttk.Entry(self.right, width=25, font=("Posterama", 20))
        #self.phone.insert(0, "Phone Number")
        self.phone.place(x=0.025 * self.right.winfo_screenwidth(), y=0.44 * self.right.winfo_screenheight()+28)

        self.label_id = Label(self.right, text="Program", font=("Posterama", 14, 'bold'), bg='#4361EE', fg='#FFFFFF')
        self.label_id.place(x=0.025 * self.right.winfo_screenwidth(), y=0.495 * self.right.winfo_screenheight()+25)

        field_list = ["Bachelor of Business Administration", "Bachelor of Management Science",
                      "Bachelor of Fashion Designing", "B.Sc- Interior Design",
                      "B.Sc.- Hospitality and Hotel Administration",
                      "Bachelor of Computer Applications", "Civil Engineering", "Automobile Engineering",
                      "Electrical and Electronics Engineering", "Bachelor of Commerce",
                      "Master of Business Administration", "Master of Mechanical Enginnering", "Master of Commerce",
                      "Master of Fashion Management", "Master of Computer Applications"]
        self.program = ttk.Combobox(self.right, values=field_list, width=28, font=("Posterama", 18, 'bold'))
        self.program.place(x=210, y=240)#self.program.insert(0, "Program")
        self.program.place(x=0.025 * self.right.winfo_screenwidth(), y=0.525 * self.right.winfo_screenheight()+25)

        self.refresh = Button(self.right, width=8, text="Clear", fg='#4361EE', font=("Posterama", 12, 'bold'), bg='#FFFFFF', command=self.registration)
        self.refresh.place(x=0.215 * self.right.winfo_screenwidth(), y=0.60 * self.right.winfo_screenheight()+25)

        self.confirm = Button(self.right, width=8, text="Confirm", fg='#4361EE', font=("Posterama", 12, 'bold'),
                              bg='#FFFFFF', command=self.reg)
        self.confirm.place(x=0.025 * self.right.winfo_screenwidth(), y=0.60 * self.right.winfo_screenheight()+25)

        self.back = Button(self.right, width=8, text="Back", fg='#4361EE', font=("Posterama", 12, 'bold'), bg='#FFFFFF', command=self.right.destroy)
        self.back.place(x=0.025 * self.right.winfo_screenwidth(), y=0.68 * self.right.winfo_screenheight())

    def reg(self):
        email_id = self.email_id.get()
        password = self.entry_password.get()
        confirm = self.confirm_password.get()
        phone = self.phone.get()
        program = self.program.get()
        if password != confirm:
            self.label_id = Label(self.right, text="X Password did not Match", font=("Posterama", 12, 'bold'), bg='#FF0000',
                                  fg='#FFFFFF')
            self.label_id.place(x=0.15 * self.right.winfo_screenwidth(),
                                y=0.330 * self.right.winfo_screenheight() + 15)
        elif email_id and password and confirm and phone and program != "":
            if '@' in email_id and '.' in email_id:
                if len(phone) == 10:
                    try:
                        query1 = "insert into 'student' (email,password,phone,program) values(?,?,?,?)"
                        cur.execute(query1, (email_id,password,phone,program))
                        con.commit()

                        #messagebox.showinfo("Success", "Registered Successfully")

                        self.right = Frame(self.master, height=0.75 * self.master.winfo_screenheight(),
                                           width=0.3 * self.master.winfo_screenwidth(), bg='#4361EE')
                        self.right.place(x=0.6 * self.master.winfo_screenwidth(), y=0.1 * self.master.winfo_screenheight())

                        self.date_lbl = Label(self.right, text="Date- " + date, font=("Posterama", 12, 'bold'), bg='#4361EE',
                                              fg='#FFFFFF')
                        self.date_lbl.place(x=0.2 * self.right.winfo_screenwidth(), y=0.01 * self.right.winfo_screenheight())
                        self.time_lbl = Label(self.right, text="Time- " + time[0] + ":" + time[1],
                                              font=("Posterama", 12, 'bold'), bg='#4361EE', fg='#FFFFFF')
                        self.time_lbl.place(x=0.2 * self.right.winfo_screenwidth(), y=0.04 * self.right.winfo_screenheight())

                        # text
                        self.label_id = Label(self.right, text="Registration \n Successful", font=("Posterama", 45, 'bold'), bg='#4361EE',
                                              fg='#FFFFFF')
                        self.label_id.place(x=0.025 * self.right.winfo_screenwidth(), y=0.08 * self.right.winfo_screenheight() + 10)

                        self.back = Button(self.right, width=8, text="Back", fg='#4361EE', font=("Posterama", 12, 'bold'),
                                           bg='#FFFFFF', command=self.right.destroy)
                        self.back.place(x=0.025 * self.right.winfo_screenwidth(), y=0.68 * self.right.winfo_screenheight())
                    except EXCEPTION as e:
                        messagebox.showerror("Error",str(e))
                else:
                    self.label_id = Label(self.right, text="Please, Enter A valid phone no.",
                                          font=("Posterama", 10, 'bold'),
                                          bg='#FF0000', fg='#FFFFFF', )
                    self.label_id.place(x=0.13 * self.right.winfo_screenwidth(), y=0.415 * self.right.winfo_screenheight()+28)
            else:
                self.label_id = Label(self.right, text="Please, Enter A valid Email ID. (It must have @ and .) ", font=("Posterama", 10, 'bold'),
                                      bg='#FF0000', fg='#FFFFFF')
                self.label_id.place(x=0.07 * self.right.winfo_screenwidth(),
                                y=0.170 * self.right.winfo_screenheight() + 15)
        else:
            self.label_id = Label(self.right, text="Please, Fill all the Fields", font=("Posterama", 18, 'bold'),
                                  bg='#FF0000',fg='#FFFFFF')
            self.label_id.place(x=0.1 * self.right.winfo_screenwidth(),
                                y=0.7 * self.right.winfo_screenheight() )

    def back(self):
        display = Application(self.master)

    def test(self):
        pass

def main():
    root = Tk()
    app = Application(root)
    root.title("Login")
    root.state("zoomed")
    root.geometry("%dx%d+0+0" % (root.winfo_screenwidth(),root.winfo_screenheight()))
    Tk.iconbitmap(root, default='images\icon_new.ico')
    root.mainloop()

if __name__=='__main__':
    main()
