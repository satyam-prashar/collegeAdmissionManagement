from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import os
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


class Admin(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))
        Tk.iconbitmap(self, default='images\icon_new.ico')
        self.state("zoomed")
        self.title('Admin')

        p1 = self.back()



    def manage_admission(self):

        self.right1 = Frame(self, height= self.winfo_screenheight(), width=0.305 * self.winfo_screenwidth(),bg='#4FFFFF')
        self.right1.place(x=0.690 * self.winfo_screenwidth(), y=0)

        my_canvas = Canvas(self.right1, height=0.940*self.winfo_screenheight(), width=0.295 * self.winfo_screenwidth(), bg='#FFFFFF')
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ttk.Scrollbar(self.right1, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        second_frame = Frame(my_canvas, height=self.winfo_screenheight(), width=0.180 * self.winfo_screenwidth(), bg='#F72585')

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        # main scroolbar work
        self.personal_frame = Frame(second_frame, height=1.2*second_frame.winfo_screenheight(), width=0.3 * self.winfo_screenwidth(), bg='#F72585')
        self.personal_frame.pack(side=TOP)


        field_list = ["Bachelor of Business Administration", "Bachelor of Management Science",
                      "Bachelor of Fashion Designing", "B.Sc- Interior Design",
                      "B.Sc.- Hospitality and Hotel Administration",
                      "Bachelor of Computer Applications", "Civil Engineering", "Automobile Engineering",
                      "Electrical and Electronics Engineering", "Bachelor of Commerce",
                      "Master of Business Administration", "Master of Mechanical Enginnering", "Master of Commerce",
                      "Master of Fashion Management", "Master of Computer Applications","Back"]

        btn_list = []
        for i in field_list:
            btn_list.append(
                Button(self.personal_frame, width=35, text=i, fg='#F72585', font=("Posterama", 14, 'bold'),
                       bg='#ffffff',activebackground = '#F72585',activeforeground = '#ffffff' , command=lambda x=i:field_operation(x)))

        for i in range(0,len(field_list)):
            btn_list[i].place(x=20, y=60*i+10)

        btn_list[len(field_list)-1].config(width= 10,font =("Posterama", 10, 'bold'),command =self.back)


        def field_operation(x):
            self.student_frame = Frame(self, height=self.winfo_screenheight(), width=0.305 * self.winfo_screenwidth(),
                                bg='#FCAED1')
            self.student_frame.place(x=0.45 * self.winfo_screenwidth(), y=0)

            my_canvas2 = Canvas(self.student_frame, height=0.940 * self.winfo_screenheight(),
                               width=0.230 * self.winfo_screenwidth(), bg='#FFFFFF')
            my_canvas2.pack(side=LEFT, fill=BOTH, expand=1)

            # Add A Scrollbar To The Canvas
            my_scrollbar2 = ttk.Scrollbar(self.student_frame, orient=VERTICAL, command=my_canvas2.yview)
            my_scrollbar2.pack(side=RIGHT, fill=Y)

            # Configure The Canvas
            my_canvas2.configure(yscrollcommand=my_scrollbar2.set)
            my_canvas2.bind('<Configure>', lambda e: my_canvas2.configure(scrollregion=my_canvas2.bbox("all")))

            # Create ANOTHER Frame INSIDE the Canvas
            second_frame2 = Frame(my_canvas2, height=self.winfo_screenheight(), width=0.230 * self.winfo_screenwidth(),
                                 bg='#FEE4F0')

            # Add that New frame To a Window In The Canvas
            my_canvas2.create_window((0, 0), window=second_frame2, anchor="nw")

            # main scroolbar work
            self.label_id = Label(second_frame2, text=x+" \n Students ", font=("Posterama", 14, 'bold'), bg='#FEE4F0', fg='#F72585')
            self.label_id.place(x=0.005 * self.winfo_screenwidth(), y=0.005 * self.winfo_screenheight())

            query = "select * from 'student' where program ='{}' Order By marks2 DESC".format(x)
            persons = cur.execute(query).fetchall()

            btn_list2 = []
            count = 1
            for person in persons:
                btn_list2.append(
                    Button(second_frame2,  text=str(count)+". "+person[2]+" "+person[3], fg='#F72585', font=("Posterama", 14, 'bold'),
                           bg='#FEE4F0', activebackground='#F72585', activeforeground='#ffffff',
                           command=lambda x2=person[0]: student_details(x2)))
                count += 1
            for i in range(0, len(persons)):
                btn_list2[i].place(x=10, y=40 * i + 100)

            def student_details(x2):
                self.detail_frame = Frame(self, height=self.winfo_screenheight(), width=0.45 * self.winfo_screenwidth(), bg='#FF00FF')
                self.detail_frame.place(x=0, y=0)

                # main frame
                # scroll bar          !!!!!!!!!!! write everything in between
                # Create A Canvas
                my_canvas3 = Canvas(self.detail_frame, height=0.94*self.winfo_screenheight(),
                                   width=0.435 * self.winfo_screenwidth(),bg='#FFFFFF')
                my_canvas3.pack(side=LEFT, fill=BOTH, expand=1)

                # Add A Scrollbar To The Canvas
                my_scrollbar3 = ttk.Scrollbar(self.detail_frame, orient=VERTICAL, command=my_canvas3.yview)
                my_scrollbar3.pack(side=RIGHT, fill=Y)

                # Configure The Canvas
                my_canvas3.configure(yscrollcommand=my_scrollbar3.set)
                my_canvas3.bind('<Configure>', lambda e: my_canvas3.configure(scrollregion=my_canvas3.bbox("all")))

                # Create ANOTHER Frame INSIDE the Canvas
                second_frame3 = Frame(my_canvas3, height=self.detail_frame.winfo_screenheight(), width=0.7 * self.detail_frame.winfo_screenwidth(),
                                     bg='#FFFFFF')

                # Add that New frame To a Window In The Canvas
                my_canvas3.create_window((0, 0), window=second_frame3, anchor="nw")

                # main scroolbar work
                self.detail1 = Frame(second_frame3, height=self.detail_frame.winfo_screenheight(), width=0.44 * self.detail_frame.winfo_screenwidth(),
                                          bg='#FFFFFF')
                self.detail1.pack(side = TOP)
                self.detail2 = Frame(second_frame3, height=self.detail_frame.winfo_screenheight(), width=0.44 * self.detail_frame.winfo_screenwidth(),
                                     bg='#FEE4F0')
                self.detail2.pack(side = TOP)
                self.detail3 = Frame(second_frame3, height=2.5*self.detail_frame.winfo_screenheight(), width=0.44 * self.detail_frame.winfo_screenwidth(),
                                     bg='#FFFFFF')
                self.detail3.pack(side = TOP)
                self.detail4 = Frame(second_frame3, height=0.5 * self.detail_frame.winfo_screenheight(),
                                     width=0.44 * self.detail_frame.winfo_screenwidth(),
                                     bg='#FEE4F0')
                self.detail4.pack(side=TOP)

                #personal Info

                self.label_id = Label(self.detail1, text="Personal Information ", font=("Posterama", 45, 'bold underline'), bg='#FFFFFF',
                                      fg='#F72585')
                self.label_id.place(x=0.025 * self.right.winfo_screenwidth(), y=0.005 * self.right.winfo_screenheight())

                query = "select * from 'student' where id ='{}'".format(x2)
                person = cur.execute(query).fetchone()

                arr1 =["Name","Surname","Father's Name","Mother's Name","Date Of Birth","Gender",
                       "Address","","City","District","State","Pincode","Category","Religion"]

                for i in range(0,len(arr1)):
                    j = i+2
                    self.label_id = Label(self.detail1, text=arr1[i], font=("Posterama", 14,), bg='#FFFFFF',
                                      fg='#F72585')
                    self.label_id.place(x=0.025 * self.right.winfo_screenwidth(), y=50*i + 0.15* self.right.winfo_screenheight())

                    self.label_id = Label(self.detail1, text=person[j], font=("Posterama", 14,), bg='#FFFFFF',
                                          fg='#000000')
                    self.label_id.place(x=0.2 * self.right.winfo_screenwidth(),
                                        y=50 * i + 0.15 * self.right.winfo_screenheight())

                ### Academic & Economic Information
                self.label_id = Label(self.detail2, text="Academic & Economic \nInformation ", font=("Posterama", 35, 'bold underline'),
                                      bg='#FEE4F0', fg='#F72585')
                self.label_id.place(x=0.025 * self.right.winfo_screenwidth(), y=0.005 * self.right.winfo_screenheight())

                arr2 = ["Father's Occupation","Mother's Occupation","Father's Income","Mother's Income","10th Class Institute","10th Class Board",
                        "10th Class Marks","12th Class Institute","12th Class Board","12th Class Marks","Degree/Diploma Institute","Degree/Diploma  Board",
                        "Degree/Diploma Marks"]

                for i in range(0,len(arr2)):
                    j = i+16
                    self.label_id = Label(self.detail2, text=arr2[i], font=("Posterama", 14,), bg='#FEE4F0',
                                      fg='#F72585')
                    self.label_id.place(x=0.025 * self.right.winfo_screenwidth(), y=50*i + 0.20* self.right.winfo_screenheight())

                    self.label_id = Label(self.detail2, text=person[j], font=("Posterama", 14,), bg='#FEE4F0',
                                          fg='#000000')
                    self.label_id.place(x=0.2 * self.right.winfo_screenwidth(),
                                        y=50 * i + 0.20 * self.right.winfo_screenheight())

                # Documents DETAILS 3
                images_present = FALSE
                try:
                    img_query = "select * from image1 where id ='{}'".format(person[0])
                    images = cur.execute(img_query).fetchall()
                    images_present = TRUE
                    for img in images:
                        storeFilePath = f"./ImageOutputs/img{img[0]}{img[1]}.jpg"
                        # print(result)
                        with open(storeFilePath, "wb") as file:
                            file.write(img[2])
                            file.close()
                except Exception as e:
                    print(str(e))

                self.label_id = Label(self.detail3, text="Documents ",
                                      font=("Posterama", 45, 'bold underline'), bg='#FFFFFF',fg='#F72585')
                self.label_id.place(x=0.025 * self.right.winfo_screenwidth(), y=0.005 * self.right.winfo_screenheight())

                field_list = ["Photo", "Signature", "Date of Birth Proof", "10th Certificate", "12th Cetificate",
                              "Degree/Diploma", "Character", "Migration"]
                for i in range(0,len(field_list)):
                    self.label_id = Label(self.detail3, text=field_list[i], font=("Posterama", 14,), bg='#FFFFFF',
                                      fg='#F72585')
                    self.label_id.place(x=0.025 * self.right.winfo_screenwidth(), y=250*i + 0.20* self.right.winfo_screenheight())


                frame_list = []
                for i in range(0, 8):
                    frame_list.append(Button(self.detail3, text="Not Found", bg='#FFFFFF', fg='#FF0000',command = lambda x=i:fullscreen(x)))
                for i in range(0, len(frame_list)):
                    frame_list[i].place(x=0.2 * self.detail3.winfo_screenwidth(),
                                        y=240 * i + 0.20 * self.detail3.winfo_screenheight())

                table_name = ["photo", "signature", "dob", "mark1", "mark2", "mark3", "character", "migration"]
                # If present adding pics to frame
                for i in range(0, len(table_name)):
                    try:
                        fln = "ImageOutputs/img{}{}.jpg".format(person[0], table_name[i])
                        img = Image.open(fln)
                        img.thumbnail((200, 200))  # for resizing
                        img = ImageTk.PhotoImage(img)
                        frame_list[i].configure(image=img,bg='#F72585')  # image
                        frame_list[i].image = img  # image
                    except Exception as e:
                        pass
                def fullscreen(x):
                    top = Toplevel(self)
                    top.title("image")
                    top.state("zoomed")
                    frame_image = Frame(top)
                    frame_image.pack(side=TOP, padx =2, pady= 2)
                    label_image = Label(frame_image)
                    label_image.pack(side = TOP)
                    top.geometry("%dx%d+0+0" % (top.winfo_screenwidth(), top.winfo_screenheight()))
                    Tk.iconbitmap(top, default='images\icon_new.ico')
                    fln = "ImageOutputs/img{}{}.jpg".format(person[0], table_name[x])
                    img = Image.open(fln)
                    img.thumbnail((top.winfo_screenwidth(), top.winfo_screenheight()))  # for resizing
                    img = ImageTk.PhotoImage(img)
                    label_image.configure(image=img, bg='#F72585')  # image
                    label_image.image = img  # image
                    top.mainloop()

                #details 4

                self.label_id = Label(self.detail4, text="Status ",
                                      font=("Posterama", 45, 'bold underline'), bg='#FEE4F0',
                                      fg='#F72585')
                self.label_id.place(x=0.025 * self.right.winfo_screenwidth(), y=0.005 * self.right.winfo_screenheight())

                field_list1 = ["Pending","Selected","Rejected"]
                self.final = ttk.Combobox(self.detail4, values=field_list1, width=28, font=("Posterama", 20,))
                self.final.insert(0,person[33])
                self.final.place(x=0.1 * self.detail4.winfo_screenwidth(),
                                        y= 0.15 * self.detail4.winfo_screenheight())

                self.submit = Button(self.detail4, width=8, text="Update", fg='#F72585', font=("Posterama", 15, 'bold'),
                                     bg='#FFFFFF', activebackground='#F72585', activeforeground='#FFFFFF',
                                     command = lambda x=person[0]:update(x))
                self.submit.place(x=0.1 * self.detail4.winfo_screenwidth(),
                                  y=0.25 * self.detail4.winfo_screenheight())
            def update(x):
                value = self.final.get()
                query = "Update student set status ='{}' where id = '{}'".format(value,x)
                cur.execute(query)
                print(x)
                con.commit()
                messagebox.showinfo("Success", "Status Updated Successfully")

    def back(self):
        self.left = Frame(self, height=self.winfo_screenheight(), width=0.700 * self.winfo_screenwidth(), bg='#FFFFFF')
        self.left.place(x=0, y=0)

        self.right = Frame(self, height=self.winfo_screenheight(), width=0.305 * self.winfo_screenwidth(), bg='#F72585')
        self.right.place(x=0.7 * self.winfo_screenwidth(), y=00)

        # buttons
        self.login = Button(self.right, width=22, text="Manage Admission", fg='#F72585', font=("Posterama", 20, 'bold'),
                            bg='#FFFFFF', command=self.manage_admission)
        self.login.place(x=0.025 * self.right.winfo_screenwidth(), y=0.2 * self.right.winfo_screenheight())

        self.message = Button(self.right, width=22, text="Massege", fg='#F72585', font=("Posterama", 20, 'bold'),
                           bg='#FFFFFF', command = self.message)
        self.message.place(x=0.025 * self.right.winfo_screenwidth(), y=0.3 * self.right.winfo_screenheight())

        self.annoucenment = Button(self.right, width=22, text="Annoucenment", fg='#F72585', font=("Posterama", 20, 'bold'),
                           bg='#FFFFFF', command = self.annoucenment_fun)
        self.annoucenment.place(x=0.025 * self.right.winfo_screenwidth(), y=0.4 * self.right.winfo_screenheight())

        self.exit = Button(self.right, width=22, text="Exit", fg='#F72585',
                                   font=("Posterama", 20, 'bold'),bg='#FFFFFF',command = self.destroy )
        self.exit.place(x=0.025 * self.right.winfo_screenwidth(), y=0.5 * self.right.winfo_screenheight())

    def message(self):
        self.message_frame = Frame(self, height=self.winfo_screenheight(), width=0.305 * self.winfo_screenwidth(),
                                   bg='#FCAED1')
        self.message_frame.place(x=0.45 * self.winfo_screenwidth(), y=0)

        my_canvas5 = Canvas(self.message_frame, height=0.940 * self.winfo_screenheight(),
                            width=0.230 * self.winfo_screenwidth(), bg='#FFFFFF')
        my_canvas5.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar2 = ttk.Scrollbar(self.message_frame, orient=VERTICAL, command=my_canvas5.yview)
        my_scrollbar2.pack(side=RIGHT, fill=Y)

        # Configure The Canvas
        my_canvas5.configure(yscrollcommand=my_scrollbar2.set)
        my_canvas5.bind('<Configure>', lambda e: my_canvas5.configure(scrollregion=my_canvas5.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        second_frame4 = Frame(my_canvas5, height=3*self.winfo_screenheight(), width=0.230 * self.winfo_screenwidth(),
                              bg='#FEE4F0')

        # Add that New frame To a Window In The Canvas
        my_canvas5.create_window((0, 0), window=second_frame4, anchor="nw")

        # main scroolbar work
        self.label_id = Label(second_frame4, text=" List of Students ", font=("Posterama", 20, 'bold underline'), bg='#FEE4F0',
                              fg='#F72585')
        self.label_id.place(x=0.005 * self.winfo_screenwidth(), y=0.005 * self.winfo_screenheight())

        self.entry_id = ttk.Entry(second_frame4, width=20, font=("Posterama", 20))
        self.entry_id.insert(0, "Search Bar", )
        self.entry_id.focus()
        self.entry_id.place(x=0.005 * self.winfo_screenwidth(), y=0.1 * self.winfo_screenheight())

        self.searchid = Button(second_frame4, width=10, text="Search by ID", fg='#F72585', font=("Posterama", 12, 'bold'),
                            bg='#FFFFFF',command = lambda i=1:search(i))
        self.searchid.place(x=0.025 * self.right.winfo_screenwidth(), y=0.15 * self.right.winfo_screenheight())

        self.searchname = Button(second_frame4, width=12, text="Search by Name", fg='#F72585', font=("Posterama", 12, 'bold'),
                               bg='#FFFFFF',command= lambda i=2:search(i) )
        self.searchname.place(x=0.1* self.right.winfo_screenwidth(), y=0.15 * self.right.winfo_screenheight())

        query = "select * from student"
        persons = cur.execute(query).fetchall()
        field_list3=[]
        for person in persons:
            field_list3.append(str(person[0])+". "+person[2]+" "+person[3])

        btn_list = []
        for i in field_list3:
            btn_list.append(
                Button(second_frame4, text=i, fg='#F72585', font=("Posterama", 14, 'bold'),
                       bg='#ffffff', activebackground='#F72585', activeforeground='#ffffff',command = lambda x=i:mess(x)))

        for i in range(0,len(field_list3)):
            btn_list[i].place(x=0.005 * self.winfo_screenwidth(), y=50*i + 0.3 * self.winfo_screenheight())

        def mess(x):
            self.display_frame = Frame(self, height=self.winfo_screenheight(), width=0.45 * self.winfo_screenwidth(),
                                       bg='#FFFFFF')
            self.display_frame.place(x=0, y=0)

            def send_message():
                x1 = x.split(".")
                message = self.message_entry.get()
                query = "insert into message (id,message,time) values(?,?,?)"
                cur.execute(query, (x1[0], message, date + " " + time))
                con.commit()
                mess(x)

            self.message_entry = ttk.Entry(self.display_frame, width=45, font=("Posterama", 20))
            self.message_entry.insert(0, "Write Message Here", )
            self.message_entry.focus()
            self.message_entry.place(x=0.001 * self.display_frame.winfo_screenwidth(),
                                     y=0.1 * self.display_frame.winfo_screenheight())

            self.enter_message = Button(self.display_frame, width=12, text="Send Message", fg='#FFFFFF',
                                        font=("Posterama", 15, 'bold'),
                                        bg='#F72585', activebackground='#FFFFFF', activeforeground='#F72585',
                                        command=send_message)
            self.enter_message.place(x=0.01 * self.display_frame.winfo_screenwidth(),
                                     y=0.15 * self.display_frame.winfo_screenheight())

            ###############################################################################

            self.message_box = Canvas(self.display_frame, height=0.55 * self.display_frame.winfo_screenheight(),
                                      width=0.45 * self.display_frame.winfo_screenwidth(), bg="#00f9fa")
            self.message_box.place(x=0.001 * self.display_frame.winfo_screenwidth(),
                                   y=0.3 * self.display_frame.winfo_screenheight())

            # scroll bar          !!!!!!!!!!! write everything in between
            # Create A Canvas
            my_canvas2 = Canvas(self.message_box, height=0.55 * self.message_box.winfo_screenheight(),
                                width=0.43 * self.message_box.winfo_screenwidth(),
                                bg='#FFFFFF')
            my_canvas2.pack(side=LEFT, fill=BOTH, expand=1)

            # Add A Scrollbar To The Canvas
            my_scrollbar2 = ttk.Scrollbar(self.message_box, orient=VERTICAL, command=my_canvas2.yview)
            my_scrollbar2.pack(side=RIGHT, fill=Y)

            # Configure The Canvas
            my_canvas2.configure(yscrollcommand=my_scrollbar2.set)
            my_canvas2.bind('<Configure>', lambda e: my_canvas2.configure(scrollregion=my_canvas2.bbox("all")))

            # Create ANOTHER Frame INSIDE the Canvas
            second_frame2 = Frame(my_canvas2, height=self.message_box.winfo_screenheight(),
                                  width=0.35 * self.message_box.winfo_screenwidth(),
                                  bg='#FFFFFF')

            # Add that New frame To a Window In The Canvas
            my_canvas2.create_window((0, 0), window=second_frame2, anchor="nw")

            x1 = x.split(".")
            try:
                query3 = "select * from message where id ='{}' ORDER BY time DESC".format(x[0])
                result3 = cur.execute(query3).fetchall()
                for i in range(0, len(result3)):
                    if i % 2 == 0:
                        self.label_name = Label(second_frame2, text=result3[i][1], font=("Posterama", 20,),
                                                width=41,
                                                fg="#000000", bg="#f8f9fa", wraplength=600)
                        self.label_name.pack(side=TOP)
                    else:
                        self.label_name = Label(second_frame2, text=result3[i][1], font=("Posterama", 20,),
                                                width=41,
                                                fg="#000000", bg="#FEE4F0", wraplength=600)
                        self.label_name.pack(side=TOP)

            except:
                self.label_name = Label(second_frame2, text="No Messege Yet", font=("Posterama", 20,), width=63,
                                        fg="#000000", bg="#f8f9fa", wraplength=1000)
                self.label_name.pack(side=TOP)

            if len(result3) == 0:
                self.label_name = Label(second_frame2, text="No Message Yet", font=("Posterama", 20,),
                                                width=41,
                                                fg="#000000", bg="#f8f9fa", wraplength=600)
                self.label_name.pack(side=TOP)
        def search(x):
            result = self.entry_id.get()
            query=""
            if x == 1:
                query = "select * from student where id = '{}'".format(result)
            elif x == 2:
                result = result.split()
                query = "select * from student where name = '{}' and surname ='{}'".format(result[0],result[1])

            self.message_frame = Frame(self, height=self.winfo_screenheight(), width=0.305 * self.winfo_screenwidth(),
                                       bg='#FCAED1')
            self.message_frame.place(x=0.45 * self.winfo_screenwidth(), y=0)

            my_canvas5 = Canvas(self.message_frame, height=0.940 * self.winfo_screenheight(),
                                width=0.230 * self.winfo_screenwidth(), bg='#FFFFFF')
            my_canvas5.pack(side=LEFT, fill=BOTH, expand=1)

            # Add A Scrollbar To The Canvas
            my_scrollbar2 = ttk.Scrollbar(self.message_frame, orient=VERTICAL, command=my_canvas5.yview)
            my_scrollbar2.pack(side=RIGHT, fill=Y)

            # Configure The Canvas
            my_canvas5.configure(yscrollcommand=my_scrollbar2.set)
            my_canvas5.bind('<Configure>', lambda e: my_canvas5.configure(scrollregion=my_canvas5.bbox("all")))

            # Create ANOTHER Frame INSIDE the Canvas
            second_frame4 = Frame(my_canvas5, height=3 * self.winfo_screenheight(),
                                  width=0.230 * self.winfo_screenwidth(),
                                  bg='#FEE4F0')

            # Add that New frame To a Window In The Canvas
            my_canvas5.create_window((0, 0), window=second_frame4, anchor="nw")

            # main scroolbar work
            self.label_id = Label(second_frame4, text=" List of Students ", font=("Posterama", 20, 'bold underline'),
                                  bg='#FEE4F0',
                                  fg='#F72585')
            self.label_id.place(x=0.005 * self.winfo_screenwidth(), y=0.005 * self.winfo_screenheight())

            self.entry_id = ttk.Entry(second_frame4, width=20, font=("Posterama", 20))
            self.entry_id.insert(0, "Search Bar", )
            self.entry_id.focus()
            self.entry_id.place(x=0.005 * self.winfo_screenwidth(), y=0.1 * self.winfo_screenheight())

            self.searchid = Button(second_frame4, width=10, text="Search by ID", fg='#F72585',
                                   font=("Posterama", 12, 'bold'),
                                   bg='#FFFFFF', command=lambda i=1: search(i))
            self.searchid.place(x=0.025 * self.right.winfo_screenwidth(), y=0.15 * self.right.winfo_screenheight())

            self.searchname = Button(second_frame4, width=12, text="Search by Name", fg='#F72585',
                                     font=("Posterama", 12, 'bold'),
                                     bg='#FFFFFF', command=lambda i=2: search(i))
            self.searchname.place(x=0.1 * self.right.winfo_screenwidth(), y=0.15 * self.right.winfo_screenheight())

            try:
                persons = cur.execute(query).fetchall()
                field_list3 = []
                for person in persons:
                    field_list3.append(str(person[0]) + ". " + person[2] + " " + person[3])

                btn_list = []
                for i in field_list3:
                    btn_list.append(
                        Button(second_frame4, text=i, fg='#F72585', font=("Posterama", 14, 'bold'),
                               bg='#ffffff', activebackground='#F72585', activeforeground='#ffffff',command = lambda x=i:mess(x)))

                for i in range(0, len(field_list3)):
                    btn_list[i].place(x=0.005 * self.winfo_screenwidth(), y=50 * i + 0.3 * self.winfo_screenheight())
            except:
                self.label_id = Label(second_frame4, text=" Sorry, Result Not Found ", font=("Posterama", 14, 'bold'),
                                      bg='#FEE4F0', fg='#F72585')
                self.label_id.place(x=0.005 * self.winfo_screenwidth(), y=0.1 * self.winfo_screenheight())

            def mess(x):
                self.display_frame = Frame(self, height=self.winfo_screenheight(), width=0.45 * self.winfo_screenwidth(),
                                          bg='#FFFFFF')
                self.display_frame.place(x=0, y=0)

                def send_message():
                    x1 = x.split(".")
                    message = self.message_entry.get()
                    query = "insert into message (id,message,time) values(?,?,?)"
                    cur.execute(query, (x1[0], message, date + " " + time))
                    con.commit()
                    mess(x)

                self.message_entry = ttk.Entry(self.display_frame, width=45,font=("Posterama", 20))
                self.message_entry.insert(0, "Write Message Here", )
                self.message_entry.focus()
                self.message_entry.place(x=0.001*self.display_frame.winfo_screenwidth(),y=0.1*self.display_frame.winfo_screenheight())

                self.enter_message = Button(self.display_frame, width=12, text="Send Message", fg='#FFFFFF',
                                            font=("Posterama", 15, 'bold'),
                                            bg='#F72585', activebackground='#FFFFFF', activeforeground='#F72585',
                                            command=send_message)
                self.enter_message.place(x=0.01*self.display_frame.winfo_screenwidth(),y=0.15*self.display_frame.winfo_screenheight())

                ###############################################################################

                self.message_box = Canvas(self.display_frame, height=0.55 * self.display_frame.winfo_screenheight(),
                                          width=0.45 * self.display_frame.winfo_screenwidth(), bg="#00f9fa")
                self.message_box.place(x=0.001 * self.display_frame.winfo_screenwidth(),
                                       y=0.3 * self.display_frame.winfo_screenheight())

                # scroll bar          !!!!!!!!!!! write everything in between
                # Create A Canvas
                my_canvas2 = Canvas(self.message_box, height=0.55 * self.message_box.winfo_screenheight(),
                                    width=0.43 * self.message_box.winfo_screenwidth(),
                                    bg='#FFFFFF')
                my_canvas2.pack(side=LEFT, fill=BOTH, expand=1)

                # Add A Scrollbar To The Canvas
                my_scrollbar2 = ttk.Scrollbar(self.message_box, orient=VERTICAL, command=my_canvas2.yview)
                my_scrollbar2.pack(side=RIGHT, fill=Y)

                # Configure The Canvas
                my_canvas2.configure(yscrollcommand=my_scrollbar2.set)
                my_canvas2.bind('<Configure>', lambda e: my_canvas2.configure(scrollregion=my_canvas2.bbox("all")))

                # Create ANOTHER Frame INSIDE the Canvas
                second_frame2 = Frame(my_canvas2, height=self.message_box.winfo_screenheight(),
                                      width=0.35 * self.message_box.winfo_screenwidth(),
                                      bg='#FFFFFF')

                # Add that New frame To a Window In The Canvas
                my_canvas2.create_window((0, 0), window=second_frame2, anchor="nw")

                x1 = x.split(".")
                try:
                    query3 = "select * from message where id ='{}' ORDER BY time DESC".format(x[0])
                    result3 = cur.execute(query3).fetchall()
                    for i in range(0, len(result3)):
                        if i % 2 == 0:
                            self.label_name = Label(second_frame2, text=result3[i][1], font=("Posterama", 20,),
                                                    width=41,
                                                    fg="#000000", bg="#f8f9fa", wraplength=600)
                            self.label_name.pack(side=TOP)
                        else:
                            self.label_name = Label(second_frame2, text=result3[i][1], font=("Posterama", 20,),
                                                    width=41,
                                                    fg="#000000", bg="#FEE4F0", wraplength=600)
                            self.label_name.pack(side=TOP)

                except:
                    self.label_name = Label(second_frame2, text="No Messege Yet", font=("Posterama", 20,), width=63,
                                            fg="#000000", bg="#f8f9fa", wraplength=1000)
                    self.label_name.pack(side=TOP)

                if len(result3) == 0:
                    self.label_name = Label(second_frame2, text="No Message Yet ", font=("Posterama", 20,),
                                                width=41,
                                                fg="#000000", bg="#f8f9fa", wraplength=600)
                    self.label_name.pack(side=TOP)

    def annoucenment_fun(self):
        self.annoucenment_frame = Frame(self, height=self.winfo_screenheight(), width=0.7 * self.winfo_screenwidth(),
                                   bg='#FFFFFF')
        self.annoucenment_frame.place(x=0, y=0)

        def send_message():
            message = self.message_entry.get()
            query = "insert into announcement (ann,time) values(?,?)"
            cur.execute(query, (message, date + " " + time))
            con.commit()
            p1 = self.annoucenment_fun()

        self.message_entry = ttk.Entry(self.annoucenment_frame, width=45, font=("Posterama", 20))
        self.message_entry.insert(0, "Write Message Here", )
        self.message_entry.focus()
        self.message_entry.place(x=0.01 * self.annoucenment_frame.winfo_screenwidth(),
                                 y=0.1 * self.annoucenment_frame.winfo_screenheight())

        self.enter_message = Button(self.annoucenment_frame, text="Send Announcement", fg='#FFFFFF',
                                    font=("Posterama", 15, 'bold'),
                                    bg='#F72585', activebackground='#FFFFFF', activeforeground='#F72585',
                                    command=send_message)
        self.enter_message.place(x=0.01 * self.annoucenment_frame.winfo_screenwidth(),
                                 y=0.15 * self.annoucenment_frame.winfo_screenheight())

        self.announcement_canvas = Canvas(self.annoucenment_frame, height=0.55 * self.annoucenment_frame.winfo_screenheight(),
                                          width=0.665 * self.annoucenment_frame.winfo_screenwidth(), bg="#f8f9fa")
        self.announcement_canvas.place(x=0.015 * self.annoucenment_frame.winfo_screenwidth(),
                                       y=0.3 * self.annoucenment_frame.winfo_screenheight())

        self.label_name = Label(self.announcement_canvas, text="Announcements", font=("Posterama", 20,), width=65,
                                fg="#FFFFFF",
                                bg="#F72585")
        self.label_name.place(x=0.001 * self.annoucenment_frame.winfo_screenwidth(),
                              y=0.001 * self.annoucenment_frame.winfo_screenheight())

        self.announcement_box = Canvas(self.announcement_canvas, height=0.35 * self.annoucenment_frame.winfo_screenheight(),
                                       width=0.665 * self.annoucenment_frame.winfo_screenwidth(), bg="#00f9fa")
        self.announcement_box.place(x=0.001 * self.annoucenment_frame.winfo_screenwidth(),
                                    y=0.045 * self.annoucenment_frame.winfo_screenheight())

        # scroll bar          !!!!!!!!!!! write everything in between
        # Create A Canvas
        my_canvas3 = Canvas(self.announcement_box, height=0.55 * self.announcement_box.winfo_screenheight(),
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

        for i in range(0, len(result4)):
            if i % 2 == 0:
                self.label_name = Label(second_frame3, text=result4[i][1], font=("Posterama", 20,), width=63,
                                        fg="#000000", bg="#f8f9fa", wraplength=1000)
                self.label_name.pack(side=TOP)
            else:
                self.label_name = Label(second_frame3, text=result4[i][1], font=("Posterama", 20,), width=63,
                                        fg="#000000", bg="#FEE4F0", wraplength=1000)
                self.label_name.pack(side=TOP)

