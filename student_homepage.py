from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import datetime
import sqlite3
from tkinter import messagebox
# we can code without using self in bottom cases
con = sqlite3.connect('student_info.db')
cur = con.cursor()
date = datetime.datetime.now().date()
date = str(date)
time = datetime.datetime.now().time()
time = str(time)


class Student_Homepage(Toplevel):
    def __init__(self,id):
        Toplevel.__init__(self)

        query = "select * from student where id ='{}'".format(id)
        result = cur.execute(query).fetchone()
        self.id = id

        query2 = "select * from dashboard where id ='{}'".format(id)
        result2 = cur.execute(query2).fetchone()
        self.id = id

        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))
        Tk.iconbitmap(self, default='images\icon_new.ico')
        self.state("zoomed")
        self.title('Student Dashboard')

        # frames
        self.left = Frame(self, height=self.winfo_screenheight(), width=0.3*self.winfo_screenwidth(),bg='#f8f9fa')
        self.left.place(x=0, y=0)

        # left frame
        try:
            img_query = "select * from image1 where id ='{}'".format(id)
            images = cur.execute(img_query).fetchall()
            images_present = TRUE
            for img in images:
                storeFilePath = f"./ImageOutputs/img{img[0]}photo.jpg"
                # print(result)
                with open(storeFilePath, "wb") as file:
                    file.write(img[2])
                    file.close()
        except Exception as e:
            print(str(e))
        fln = "ImageOutputs/img{}photo.jpg".format(self.id)
        img = Image.open(fln)
        img.thumbnail((200, 200))
        img = ImageTk.PhotoImage(img)

        self.photo_label = Label(self.left, font=("Posterama", 14,))
        self.photo_label.place(x=0.01 * self.winfo_screenwidth(), y=0.01 * self.winfo_screenheight())
        self.photo_label.configure(image=img)  # image
        self.photo_label.image = img  # image

        self.label_name = Label(self.left, text="Welcome", font=("Posterama", 10,), fg="#000000", bg="#f8f9fa")
        self.label_name.place(x=0.15 * self.winfo_screenwidth(), y=0.05 * self.winfo_screenheight())

        self.label_name = Label(self.left, text=result[2] + " " + result[3], font=("Posterama", 20,), fg="#4361EE",
                                bg="#f8f9fa")
        self.label_name.place(x=0.15 * self.winfo_screenwidth(), y=0.08 * self.winfo_screenheight())

        self.label_name = Label(self.left, text="ID: " + str(result[0]), font=("Posterama", 16,), fg="#000000",
                                bg="#f8f9fa")
        self.label_name.place(x=0.15 * self.winfo_screenwidth(), y=0.13 * self.winfo_screenheight())

        ##################################################################################################
        self.class_canvas = Canvas(self.left, height=0.2 * self.left.winfo_screenheight(),
                                   width=0.28 * self.left.winfo_screenwidth(), bg='#f8f9fa')
        self.class_canvas.place(x=0.01 * self.winfo_screenwidth(), y=0.23 * self.winfo_screenheight())

        self.label_name = Label(self.class_canvas, text="Program", font=("Posterama", 14,), fg="#000000", bg="#f8f9fa")
        self.label_name.place(x=0.01 * self.class_canvas.winfo_screenwidth(),
                              y=0.03 * self.class_canvas.winfo_screenheight())

        self.label_name = Label(self.class_canvas, text=result[32], font=("Posterama", 14,), fg="#4361EE", bg="#f8f9fa",
                                wraplength=200)
        self.label_name.place(x=0.1 * self.class_canvas.winfo_screenwidth(),
                              y=0.01 * self.class_canvas.winfo_screenheight())

        self.label_name = Label(self.class_canvas, text="Section", font=("Posterama", 14,), fg="#000000", bg="#f8f9fa")
        self.label_name.place(x=0.01 * self.class_canvas.winfo_screenwidth(),
                              y=0.1 * self.class_canvas.winfo_screenheight())

        self.label_name = Label(self.class_canvas, text=result2[2], font=("Posterama", 14,), fg="#4361EE", bg="#f8f9fa")
        self.label_name.place(x=0.15 * self.class_canvas.winfo_screenwidth(),
                              y=0.1 * self.class_canvas.winfo_screenheight())

        self.label_name = Label(self.class_canvas, text="Roll No", font=("Posterama", 14,), fg="#000000", bg="#f8f9fa")
        self.label_name.place(x=0.01 * self.class_canvas.winfo_screenwidth(),
                              y=0.16 * self.class_canvas.winfo_screenheight())

        self.label_name = Label(self.class_canvas, text=result2[3], font=("Posterama", 14,), fg="#4361EE", bg="#f8f9fa")
        self.label_name.place(x=0.15 * self.class_canvas.winfo_screenwidth(),
                              y=0.16 * self.class_canvas.winfo_screenheight())

        ###############################################################################
        self.TOD_canvas = Canvas(self.left, height=0.2 * self.left.winfo_screenheight(),
                                 width=0.28 * self.left.winfo_screenwidth(), bg='#f8f9fa')
        self.TOD_canvas.place(x=0.01 * self.winfo_screenwidth(), y=0.45 * self.winfo_screenheight())

        self.label_name = Label(self.TOD_canvas, text="Tip Of Day", font=("Posterama", 20,), fg="#000000", bg="#f8f9fa")
        self.label_name.place(x=0.08 * self.TOD_canvas.winfo_screenwidth(),
                              y=0.001 * self.TOD_canvas.winfo_screenheight())

        ###############################################################################
        self.info_canvas = Canvas(self.left, height=0.2 * self.left.winfo_screenheight(),
                                  width=0.28 * self.left.winfo_screenwidth(), bg='#f8f9fa')
        self.info_canvas.place(x=0.01 * self.winfo_screenwidth(), y=0.67 * self.winfo_screenheight())

        self.label_name = Label(self.info_canvas, text="Important Imformation", font=("Posterama", 20,), fg="#000000",
                                bg="#f8f9fa")
        self.label_name.place(x=0.04 * self.info_canvas.winfo_screenwidth(),
                              y=0.001 * self.info_canvas.winfo_screenheight())

        p1 = self.home()

    def home(self):
        self.right = Frame(self, height=self.winfo_screenheight(), width=0.7 * self.winfo_screenwidth(),bg='#FFFFFF')
        self.right.place(x=0.3*self.winfo_screenwidth(), y=0)


        ############################################################################################################################

        #right frame
        #scroll bar          !!!!!!!!!!! write everything in between
        # Create A Canvas
        my_canvas = Canvas(self.right, height=0.944*self.winfo_screenheight(), width=0.685 * self.winfo_screenwidth(),bg='#FFFFFF')
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(self.right, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        second_frame = Frame(my_canvas, height=self.winfo_screenheight(), width=0.7 * self.winfo_screenwidth(),bg='#FFFFFF')

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        # main scroolbar work
        self.taskbar_frame = Canvas(second_frame, height=0.05*second_frame.winfo_screenheight(),
                                                width=0.9 * self.winfo_screenwidth(), bg='#4361EE')
        self.taskbar_frame.pack(side=TOP)

        self.home_frame = self.main = Frame(second_frame, height=1.5*second_frame.winfo_screenheight(),
                                                width=0.9 * self.winfo_screenwidth(), bg='#FFFFFF')
        self.home_frame.pack(side=TOP)

        task_bar_txt = ["Home","Learning","Finance","Important Links","Sign Out"]
        task_bar_btn = []
        for i in range(0, len(task_bar_txt)):
            task_bar_btn.append(
                Button(self.taskbar_frame, text=task_bar_txt[i], bg='#FFFFFF', fg='#4361EE',font=("Posterama", 14,) ))
            task_bar_btn[i].place(x=50+1.4*i*0.1*self.right.winfo_screenwidth(),y = 0.004* self.right.winfo_screenheight())

        task_bar_btn[0].config(command=self.home)
        task_bar_btn[1].config(command=self.learning)
        task_bar_btn[2].config(command=self.finance)
        task_bar_btn[3].config(command=self.important)
        task_bar_btn[4].config(command=self.destroy)

        ###############################################################################################################

        self.label_name = Label(self.home_frame, text="Home", font=("Posterama", 34,), fg="#4361EE", bg="#FFFFFF")
        self.label_name.place(x=0.01 * self.home_frame.winfo_screenwidth(),
                              y=0.001 * self.home_frame.winfo_screenheight())

        #########################################################

        self.time_table = Canvas(self.home_frame,height = 0.4*self.home_frame.winfo_screenheight(),width = 0.665*self.home_frame.winfo_screenwidth(), bg="#f8f9fa")
        self.time_table.place(x=0.01 * self.home_frame.winfo_screenwidth(),
                              y=0.07 * self.home_frame.winfo_screenheight())

        self.label_name = Label(self.time_table, text="Time Table", font=("Posterama", 20,),width = 65, fg="#FFFFFF", bg="#4361EE")
        self.label_name.place(x=0.001 * self.home_frame.winfo_screenwidth(),
                              y=0.001 * self.home_frame.winfo_screenheight())


        self.label_name = Label(self.time_table, text="9 a.m. - 10 a.m.                       Physics                        Mr. Sudha Shankar",
                                font=("Posterama", 20,), width=65, fg="#000000",
                                bg="#E9F8FD")
        self.label_name.place(x=0.001 * self.home_frame.winfo_screenwidth(),
                              y=0.05 * self.home_frame.winfo_screenheight())

        self.label_name = Label(self.time_table,
                                text="11 a.m. - 12 Noon                       Chemistry                        Mr. Sudha Shankar",
                                font=("Posterama", 20,), width=65, fg="#000000",
                                bg="#f8f9fa")
        self.label_name.place(x=0.001 * self.home_frame.winfo_screenwidth(),
                              y=0.1 * self.home_frame.winfo_screenheight())

        self.label_name = Label(self.time_table, text="12 Noon - 1 p.m.                       Physics                        Mr. Sudha Shankar",
                                font=("Posterama", 20,), width=65, fg="#000000",
                                bg="#E9F8FD")
        self.label_name.place(x=0.001 * self.home_frame.winfo_screenwidth(),
                              y=0.15 * self.home_frame.winfo_screenheight())

        self.label_name = Label(self.time_table,
                                text="2 p.m. - 3 p.m.                       Chemistry                        Mr. Sudha Shankar",
                                font=("Posterama", 20,), width=65, fg="#000000",
                                bg="#f8f9fa")
        self.label_name.place(x=0.001 * self.home_frame.winfo_screenwidth(),
                              y=0.2 * self.home_frame.winfo_screenheight())

        self.label_name = Label(self.time_table,
                                text="3 p.m. - 4 p.m.                       Physics                        Mr. Sudha Shankar",
                                font=("Posterama", 20,), width=65, fg="#000000",
                                bg="#E9F8FD")
        self.label_name.place(x=0.001 * self.home_frame.winfo_screenwidth(),
                              y=0.25 * self.home_frame.winfo_screenheight())

        self.label_name = Label(self.time_table,
                                text="4 p.m. - 5 p.m.                       Chemistry                        Mr. Sudha Shankar",
                                font=("Posterama", 20,), width=65, fg="#000000",
                                bg="#f8f9fa")
        self.label_name.place(x=0.001 * self.home_frame.winfo_screenwidth(),
                              y=0.3 * self.home_frame.winfo_screenheight())

        self.label_name = Label(self.time_table,
                                text="11 a.m. - 12 a.m.                       Physics                        Mr. Sudha Shankar",
                                font=("Posterama", 20,), width=65, fg="#000000",
                                bg="#E9F8FD")
        self.label_name.place(x=0.001 * self.home_frame.winfo_screenwidth(),
                              y=0.35 * self.home_frame.winfo_screenheight())


        ########################################################################################
        self.message_canvas = Canvas(self.home_frame, height=0.4 * self.home_frame.winfo_screenheight(),
                                 width=0.665 * self.home_frame.winfo_screenwidth(), bg="#f8f9fa")
        self.message_canvas.place(x=0.01 * self.home_frame.winfo_screenwidth(),
                              y=0.5 * self.home_frame.winfo_screenheight())

        self.label_name = Label(self.message_canvas, text="Message", font=("Posterama", 20,), width=65, fg="#FFFFFF",
                                bg="#4361EE")
        self.label_name.place(x=0.001 * self.home_frame.winfo_screenwidth(),
                              y=0.001 * self.home_frame.winfo_screenheight())

        self.message_box = Canvas(self.message_canvas, height=0.35 * self.home_frame.winfo_screenheight(),
                                 width=0.665 * self.home_frame.winfo_screenwidth(), bg="#00f9fa")
        self.message_box.place(x=0.001 * self.home_frame.winfo_screenwidth(),
                              y=0.045 * self.home_frame.winfo_screenheight())

        # scroll bar          !!!!!!!!!!! write everything in between
        # Create A Canvas
        my_canvas2 = Canvas(self.message_box, height=0.35 * self.message_box.winfo_screenheight(), width=0.65 * self.message_box.winfo_screenwidth(),
                           bg='#FFFFFF')
        my_canvas2.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar2 = ttk.Scrollbar(self.message_box, orient=VERTICAL, command=my_canvas2.yview)
        my_scrollbar2.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas2.configure(yscrollcommand=my_scrollbar2.set)
        my_canvas2.bind('<Configure>', lambda e: my_canvas2.configure(scrollregion=my_canvas2.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        second_frame2 = Frame(my_canvas2, height=self.message_box.winfo_screenheight(), width=0.65 * self.message_box.winfo_screenwidth(),
                             bg='#FFFFFF')

        # Add that New frame To a Window In The Canvas
        my_canvas2.create_window((0, 0), window=second_frame2, anchor="nw")

        try:
            query3 = "select * from message where id ='{}' ORDER BY time DESC".format(self.id)
            result3 = cur.execute(query3).fetchall()
            for i in range(0, len(result3)):
                if i % 2 == 0:
                    self.label_name = Label(second_frame2, text=result3[i][1], font=("Posterama", 20,), width=63,
                                            fg="#000000", bg="#f8f9fa", wraplength=1000)
                    self.label_name.pack(side=TOP)
                else:
                    self.label_name = Label(second_frame2, text=result3[i][1], font=("Posterama", 20,), width=63,
                                            fg="#000000", bg="#E9F8FD", wraplength=1000)
                    self.label_name.pack(side=TOP)

        except:
            self.label_name = Label(second_frame2, text="No Messege Yet", font=("Posterama", 20,), width=63,
                                    fg="#000000", bg="#f8f9fa", wraplength=1000)
            self.label_name.pack(side=TOP)

        if len(result3) == 0:
            self.label_name = Label(second_frame2, text="No Messege Yet", font=("Posterama", 20,), width=63,
                                    fg="#000000", bg="#f8f9fa", wraplength=1000)
            self.label_name.pack(side=TOP)


        ########################################################################################
        self.announcement_canvas = Canvas(self.home_frame, height=0.4 * self.home_frame.winfo_screenheight(),
                                     width=0.665 * self.home_frame.winfo_screenwidth(), bg="#f8f9fa")
        self.announcement_canvas.place(x=0.01 * self.home_frame.winfo_screenwidth(),
                                  y=0.94 * self.home_frame.winfo_screenheight())

        self.label_name = Label(self.announcement_canvas, text="Announcements", font=("Posterama", 20,), width=65, fg="#FFFFFF",
                                bg="#4361EE")
        self.label_name.place(x=0.001 * self.home_frame.winfo_screenwidth(),
                              y=0.001 * self.home_frame.winfo_screenheight())

        self.announcement_box = Canvas(self.announcement_canvas, height=0.35 * self.home_frame.winfo_screenheight(),
                                  width=0.665 * self.home_frame.winfo_screenwidth(), bg="#00f9fa")
        self.announcement_box.place(x=0.001 * self.home_frame.winfo_screenwidth(),
                               y=0.045 * self.home_frame.winfo_screenheight())

        # scroll bar          !!!!!!!!!!! write everything in between
        # Create A Canvas
        my_canvas3 = Canvas(self.announcement_box, height=0.35 * self.announcement_box.winfo_screenheight(),
                            width=0.65 * self.announcement_box.winfo_screenwidth(),
                            bg='#FFFFFF')
        my_canvas3.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar3 = ttk.Scrollbar(self.announcement_box, orient=VERTICAL, command=my_canvas3.yview)
        my_scrollbar3.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas3.configure(yscrollcommand=my_scrollbar3.set)
        my_canvas3.bind('<Configure>', lambda e: my_canvas3.configure(scrollregion=my_canvas3.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        second_frame3 = Frame(my_canvas3, height=self.announcement_box.winfo_screenheight(),
                              width=0.65 * self.announcement_box.winfo_screenwidth(),
                              bg='#FFFFFF')

        # Add that New frame To a Window In The Canvas
        my_canvas3.create_window((0, 0), window=second_frame3, anchor="nw")

        query4 = "select * from announcement ORDER BY sr DESC"
        result4 = cur.execute(query4).fetchall()

        for i in range(0,len(result4)):
            if i%2 ==0:
                self.label_name = Label(second_frame3, text=result4[i][1], font=("Posterama", 20,), width=63,
                                    fg="#000000", bg="#f8f9fa", wraplength = 1000)
                self.label_name.pack(side = TOP)
            else:
                self.label_name = Label(second_frame3, text=result4[i][1], font=("Posterama", 20,), width=63,
                                    fg="#000000", bg="#E9F8FD", wraplength = 1000)
                self.label_name.pack(side = TOP)

        ################################################################################################################

    def learning(self):
            self.right = Frame(self, height=self.winfo_screenheight(), width=0.7 * self.winfo_screenwidth(),
                               bg='#FFFFFF')
            self.right.place(x=0.3 * self.winfo_screenwidth(), y=0)

            ############################################################################################################################

            # right frame
            # scroll bar          !!!!!!!!!!! write everything in between
            # Create A Canvas
            my_canvas = Canvas(self.right, height=0.944 * self.winfo_screenheight(),
                               width=0.685 * self.winfo_screenwidth(), bg='#FFFFFF')
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

            # Add A Scrollbar To The Canvas
            my_scrollbar = ttk.Scrollbar(self.right, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)

            # Configure The Canvas
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

            # Create ANOTHER Frame INSIDE the Canvas
            second_frame = Frame(my_canvas, height=self.winfo_screenheight(), width=0.7 * self.winfo_screenwidth(),
                                 bg='#FFFFFF')

            # Add that New frame To a Window In The Canvas
            my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

            # main scroolbar work
            self.taskbar_frame = Canvas(second_frame, height=0.05 * second_frame.winfo_screenheight(),
                                        width=0.9 * self.winfo_screenwidth(), bg='#4361EE')
            self.taskbar_frame.pack(side=TOP)

            self.home_frame = self.main = Frame(second_frame, height=1.5 * second_frame.winfo_screenheight(),
                                                width=0.9 * self.winfo_screenwidth(), bg='#FFFFFF')
            self.home_frame.pack(side=TOP)

            task_bar_txt = ["Home", "Learning", "Finance", "Important Links", "Sign Out"]
            task_bar_btn = []
            for i in range(0, len(task_bar_txt)):
                task_bar_btn.append(
                    Button(self.taskbar_frame, text=task_bar_txt[i], bg='#FFFFFF', fg='#4361EE',
                           font=("Posterama", 14,)))
                task_bar_btn[i].place(x=50 + 1.4 * i * 0.1 * self.right.winfo_screenwidth(),
                                      y=0.004 * self.right.winfo_screenheight())

            task_bar_btn[0].config(command=self.home)
            task_bar_btn[1].config(command=self.learning)
            task_bar_btn[2].config(command=self.finance)
            task_bar_btn[3].config(command=self.important)
            task_bar_btn[4].config(command=self.destroy)
            ###############################################################################################################

            self.label_name = Label(self.home_frame, text="Learning", font=("Posterama", 34,), fg="#4361EE", bg="#FFFFFF")
            self.label_name.place(x=0.01 * self.home_frame.winfo_screenwidth(),
                                  y=0.001 * self.home_frame.winfo_screenheight())

        ############################################################################################################
            self.attendence = Canvas(self.home_frame, height=0.4 * self.home_frame.winfo_screenheight(),
                                     width=0.665 * self.home_frame.winfo_screenwidth(), bg="#f8f9fa")
            self.attendence.place(x=0.01 * self.home_frame.winfo_screenwidth(),
                                  y=0.07 * self.home_frame.winfo_screenheight())

            self.label_name = Label(self.attendence, text="Attendence", font=("Posterama", 20,), width=65, fg="#FFFFFF",
                                    bg="#4361EE")
            self.label_name.place(x=0.001 * self.home_frame.winfo_screenwidth(),
                                  y=0.001 * self.home_frame.winfo_screenheight())
        #############################################################################################################
            self.assignment = Canvas(self.home_frame, height=0.4 * self.home_frame.winfo_screenheight(),
                                     width=0.665 * self.home_frame.winfo_screenwidth(), bg="#f8f9fa")
            self.assignment.place(x=0.01 * self.home_frame.winfo_screenwidth(),
                                  y=0.5 * self.home_frame.winfo_screenheight())

            self.label_name = Label(self.assignment, text="Assignment", font=("Posterama", 20,), width=65, fg="#FFFFFF",
                                    bg="#4361EE")
            self.label_name.place(x=0.001 * self.home_frame.winfo_screenwidth(),
                                  y=0.001 * self.home_frame.winfo_screenheight())

            #############################################################################################################
            self.buttons = Canvas(self.home_frame, height=0.4 * self.home_frame.winfo_screenheight(),
                                     width=0.665 * self.home_frame.winfo_screenwidth(), bg="#f8f9fa")
            self.buttons.place(x=0.01 * self.home_frame.winfo_screenwidth(),
                                  y=0.5 * self.home_frame.winfo_screenheight())

            btn_test_arr = ["Download Questions Paper","Uploading Question Paper","Verification of Answer Sheet",
                            "Download Study material","Old Question paper","Result Instruction","Fill Exam Form","Apply Answer Sheet PDF"
                            ,"Re-Evaluation Form",]
            btn_arr = []
            for i in btn_test_arr:
                btn_arr.append(Button(self.buttons,text=i, bg="#4361EE",fg="#FFFFFF",font=("Posterama", 12,),wraplength = 200))
            j = 1
            k = 0
            for i in range(0,len(btn_test_arr)):
                if i%3 ==0:
                    j = 1
                    k = k + 50
                btn_arr[i].place(x=j*0.01 * self.home_frame.winfo_screenwidth(),
                                  y=k* 0.001 * self.home_frame.winfo_screenheight())
                j += 25


    def finance(self):
            self.right = Frame(self, height=self.winfo_screenheight(), width=0.7 * self.winfo_screenwidth(),
                               bg='#FFFFFF')
            self.right.place(x=0.3 * self.winfo_screenwidth(), y=0)

            ############################################################################################################################

            # right frame
            # scroll bar          !!!!!!!!!!! write everything in between
            # Create A Canvas
            my_canvas = Canvas(self.right, height=0.944 * self.winfo_screenheight(),
                               width=0.685 * self.winfo_screenwidth(), bg='#FFFFFF')
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

            # Add A Scrollbar To The Canvas
            my_scrollbar = ttk.Scrollbar(self.right, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)

            # Configure The Canvas
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

            # Create ANOTHER Frame INSIDE the Canvas
            second_frame = Frame(my_canvas, height=self.winfo_screenheight(), width=0.7 * self.winfo_screenwidth(),
                                 bg='#FFFFFF')

            # Add that New frame To a Window In The Canvas
            my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

            # main scroolbar work
            self.taskbar_frame = Canvas(second_frame, height=0.05 * second_frame.winfo_screenheight(),
                                        width=0.9 * self.winfo_screenwidth(), bg='#4361EE')
            self.taskbar_frame.pack(side=TOP)

            self.home_frame = self.main = Frame(second_frame, height=1.5 * second_frame.winfo_screenheight(),
                                                width=0.9 * self.winfo_screenwidth(), bg='#FFFFFF')
            self.home_frame.pack(side=TOP)

            task_bar_txt = ["Home", "Learning", "Finance", "Important Links", "Sign Out"]
            task_bar_btn = []
            for i in range(0, len(task_bar_txt)):
                task_bar_btn.append(
                    Button(self.taskbar_frame, text=task_bar_txt[i], bg='#FFFFFF', fg='#4361EE',
                           font=("Posterama", 14,)))
                task_bar_btn[i].place(x=50 + 1.4 * i * 0.1 * self.right.winfo_screenwidth(),
                                      y=0.004 * self.right.winfo_screenheight())

            task_bar_btn[0].config(command=self.home)
            task_bar_btn[1].config(command=self.learning)
            task_bar_btn[2].config(command=self.finance)
            task_bar_btn[3].config(command=self.important)
            task_bar_btn[4].config(command=self.destroy)
            ###############################################################################################################

            self.label_name = Label(self.home_frame, text="Finance", font=("Posterama", 34,), fg="#4361EE", bg="#FFFFFF")
            self.label_name.place(x=0.01 * self.home_frame.winfo_screenwidth(),
                                  y=0.001 * self.home_frame.winfo_screenheight())

    def important(self):
            self.right = Frame(self, height=self.winfo_screenheight(), width=0.7 * self.winfo_screenwidth(),
                               bg='#FFFFFF')
            self.right.place(x=0.3 * self.winfo_screenwidth(), y=0)

            ############################################################################################################################

            # right frame
            # scroll bar          !!!!!!!!!!! write everything in between
            # Create A Canvas
            my_canvas = Canvas(self.right, height=0.944 * self.winfo_screenheight(),
                               width=0.685 * self.winfo_screenwidth(), bg='#FFFFFF')
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

            # Add A Scrollbar To The Canvas
            my_scrollbar = ttk.Scrollbar(self.right, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)

            # Configure The Canvas
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

            # Create ANOTHER Frame INSIDE the Canvas
            second_frame = Frame(my_canvas, height=self.winfo_screenheight(), width=0.7 * self.winfo_screenwidth(),
                                 bg='#FFFFFF')

            # Add that New frame To a Window In The Canvas
            my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

            # main scroolbar work
            self.taskbar_frame = Canvas(second_frame, height=0.05 * second_frame.winfo_screenheight(),
                                        width=0.9 * self.winfo_screenwidth(), bg='#4361EE')
            self.taskbar_frame.pack(side=TOP)

            self.home_frame = self.main = Frame(second_frame, height=1.5 * second_frame.winfo_screenheight(),
                                                width=0.9 * self.winfo_screenwidth(), bg='#FFFFFF')
            self.home_frame.pack(side=TOP)

            task_bar_txt = ["Home", "Learning", "Finance", "Important Links", "Sign Out"]
            task_bar_btn = []
            for i in range(0, len(task_bar_txt)):
                task_bar_btn.append(
                    Button(self.taskbar_frame, text=task_bar_txt[i], bg='#FFFFFF', fg='#4361EE',
                           font=("Posterama", 14,)))
                task_bar_btn[i].place(x=50 + 1.4 * i * 0.1 * self.right.winfo_screenwidth(),
                                      y=0.004 * self.right.winfo_screenheight())

            task_bar_btn[0].config(command=self.home)
            task_bar_btn[1].config(command=self.learning)
            task_bar_btn[2].config(command=self.finance)
            task_bar_btn[3].config(command=self.important)
            task_bar_btn[4].config(command=self.destroy)

            ###############################################################################################################

            self.label_name = Label(self.home_frame, text="Important Links", font=("Posterama", 34,), fg="#4361EE", bg="#FFFFFF")
            self.label_name.place(x=0.01 * self.home_frame.winfo_screenwidth(),
                                  y=0.001 * self.home_frame.winfo_screenheight())


