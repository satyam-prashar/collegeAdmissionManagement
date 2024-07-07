from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import random
import datetime
date = datetime.datetime.now().date()
date = str(date)

class Fees_Structure(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))
        Tk.iconbitmap(self, default='images\icon_new.ico')
        self.state("zoomed")
        self.title('Fees Structure')

        self.top_image = PhotoImage(file="images/About Us_image.png")
        self.top_image_label = Label(self, image=self.top_image, bg="#FFFFFF")
        self.top_image_label.place(x=-5, y=-5)

        self.main = Frame(self, height=2*self.winfo_screenheight(), width=0.9 * self.winfo_screenwidth(), bg='#FFFFFF')
        self.main.place(x=0.15 * self.winfo_screenwidth(), y=0.1 * self.winfo_screenheight())
        # main frame
        # scroll bar          !!!!!!!!!!! write everything in between
        # Create A Canvas
        my_canvas = Canvas(self.main, height=0.83 * self.winfo_screenheight(), width=0.685 * self.winfo_screenwidth(),
                           bg='#FFFFFF')
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(self.main, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        second_frame = Frame(my_canvas, height=2*my_canvas.winfo_screenheight(), width=0.7 * my_canvas.winfo_screenwidth(),bg='#FFFFFF')

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        # main scroolbar work

        my_canvas2 = Canvas(second_frame, height=2*second_frame.winfo_screenheight(), width=second_frame.winfo_screenwidth(), bg='#FFFFFF')
        my_canvas2.pack(side=TOP, fill=BOTH, expand=0)

        field_list = ["Bachelor of Business Administration", "Bachelor of Management Science",
                      "Bachelor of Fashion Designing", "B.Sc- Interior Design",
                      "B.Sc.- Hospitality and Hotel Administration",
                      "Bachelor of Computer Applications", "Civil Engineering", "Automobile Engineering",
                      "Electrical and Electronics Engineering", "Bachelor of Commerce",
                      "Master of Business Administration", "Master of Mechanical Enginnering", "Master of Commerce",
                      "Master of Fashion Management", "Master of Computer Applications"]

        fees = []
        for i in range(0,len(field_list)):
            temp = random.randint(40,60)
            fees.append(temp*1000)

        self.personal = Label(my_canvas2, text="Fees Structure ", font=("Posterama", 45, 'underline'), bg='#FFFFFF', fg='#4361EE')
        self.personal.place(x=20, y=20)

        for i in range(0,len(field_list)):
            self.personal2 = Label(my_canvas2, text=field_list[i], font=("Posterama", 20,), bg='#FFFFFF', fg='#000000')
            self.personal2.place(x=30, y=i*50+150)
            my_canvas2.create_line(20, 145+i*50, 0.6 * my_canvas.winfo_screenwidth(), 145+i*50)

        for i in range(0,len(fees)):
            self.personal2 = Label(my_canvas2, text=fees[i], font=("Posterama", 20,), bg='#FFFFFF', fg='#000000')
            self.personal2.place(x=0.5 * my_canvas.winfo_screenwidth(), y=i * 50 + 150)

        #completing rectangle
        my_canvas2.create_line(20, 145 + len(field_list) * 50, 0.6 * my_canvas.winfo_screenwidth(), 145 + len(field_list) * 50)
        my_canvas2.create_line(20, 145, 20,145 + len(field_list) * 50)
        my_canvas2.create_line(0.45 * my_canvas.winfo_screenwidth(), 145, 0.45 * my_canvas.winfo_screenwidth(),145 + len(field_list) * 50)
        my_canvas2.create_line(0.6 * my_canvas.winfo_screenwidth(), 145, 0.6 * my_canvas.winfo_screenwidth(), 145 + len(field_list) * 50)
