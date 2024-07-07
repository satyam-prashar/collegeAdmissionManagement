from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import datetime
date = datetime.datetime.now().date()
date = str(date)

class About_Us(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))
        Tk.iconbitmap(self, default='images\icon_new.ico')
        self.state("zoomed")
        self.title('About Us')

        self.main = Frame(self, height=self.winfo_screenheight(), width=0.9 * self.winfo_screenwidth(), bg='#FFFFFF')
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
        second_frame = Frame(my_canvas, height=self.winfo_screenheight(), width=0.7 * self.winfo_screenwidth(),bg='#FFFFFF')

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        # main scroolbar work
        self.personal_frame= self.main = Frame(second_frame, height=0.5*second_frame.winfo_screenheight(), width=0.9 * self.winfo_screenwidth(), bg='#FFFFFF')
        self.personal_frame.pack(side= TOP)

        self.academic_frame = self.main = Frame(second_frame, height=0.5* second_frame.winfo_screenheight(),width=0.9 * self.winfo_screenwidth(), bg='#4361EE')
        self.academic_frame.pack(side=TOP)

        self.document_frame = self.main = Frame(second_frame, height=0.5*second_frame.winfo_screenheight(),width=0.9 * self.winfo_screenwidth(), bg='#FFFFFF')
        self.document_frame.pack(side=TOP)

        #personal frame First frame
        self.first_left_frame = self.main = Frame(self.personal_frame, height=0.5*second_frame.winfo_screenheight(), width=0.25 * self.winfo_screenwidth(), bg='#FFFFFF')
        self.first_left_frame.pack(side=LEFT)

        self.first_right_frame = self.main = Frame(self.personal_frame, height=0.5*second_frame.winfo_screenheight(),width=0.75 * self.winfo_screenwidth(), bg='#B5179E')
        self.first_right_frame.pack(side=RIGHT)

        self.personal = Label(self.first_right_frame, text="Who Are We ", font=("Posterama", 35, 'underline'), bg='#B5179E', fg='#FFFFFF')
        self.personal.place(x=0.05 * self.first_right_frame.winfo_screenwidth(), y=0.05 * self.first_right_frame.winfo_screenheight())

        about = "Aldridge College University is one of Canada's best known\ninstitutions of higher learning and one of the " \
                "leading\nuniversities in the world. With students coming " \
                "to Aldridge\nCollege from over 150 countries, our student " \
                "body is the\nmost internationally diverse of any research " \
                "\n-intensive university in the country."

        self.personal = Label(self.first_right_frame, text=about, font=("Posterama", 18,), bg='#B5179E', fg='#FFFFFF')
        self.personal.place(x=0.05 * self.first_right_frame.winfo_screenwidth(), y=0.2 * self.first_right_frame.winfo_screenheight())

        # academic frame second frame

        self.second_left_frame = self.main = Frame(self.academic_frame, height=0.5*second_frame.winfo_screenheight(),width=0.75 * self.winfo_screenwidth(), bg='#7209B7')
        self.second_left_frame.pack(side=LEFT)

        self.second_right_frame = self.main = Frame(self.academic_frame, height=0.5*second_frame.winfo_screenheight(), width=0.25 * self.winfo_screenwidth(), bg='#FFFFFF')
        self.second_right_frame.pack(side=RIGHT)

        # document frame third frame

        self.third_left_frame = self.main = Frame(self.document_frame, height=0.5*second_frame.winfo_screenheight(),width=0.25 * self.winfo_screenwidth(), bg='#FFFFFF')
        self.third_left_frame.pack(side=LEFT)

        self.third_right_frame = self.main = Frame(self.document_frame, height=0.5*second_frame.winfo_screenheight(),width=0.75 * self.winfo_screenwidth(), bg='#B5179E')
        self.third_right_frame.pack(side=RIGHT)
