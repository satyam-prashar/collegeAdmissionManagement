from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
from PIL import Image, ImageTk

from tkinter import ttk
import sqlite3
import datetime
import sqlite3
from tkinter import messagebox
# we can code without using self in bottom cases
con = sqlite3.connect('student_info.db')
cur = con.cursor()

date = datetime.datetime.now().date()
date = str(date)

class Form(Toplevel):
    def __init__(self,id):
        Toplevel.__init__(self)
        self.geometry("%dx%d+0+0" % (self.winfo_screenwidth(), self.winfo_screenheight()))
        Tk.iconbitmap(self, default='images\icon_new.ico')
        self.state("zoomed")
        self.title('Form')

        # background image
        self.top_image = PhotoImage(file="images/college1.png")
        self.top_image_label = Label(self, image=self.top_image, bg="#FFFFFF")
        self.top_image_label.place(x=-5, y=-5)

        query = "select * from student where id ='{}'".format(id)
        result = cur.execute(query).fetchone()
        self.id = id

        images_present = FALSE
        try:
            img_query = "select * from image1 where id ='{}'".format(id)
            images = cur.execute(img_query).fetchall()
            images_present = TRUE
            for img in images:
                storeFilePath = f"./ImageOutputs/img{img[0]}{img[1]}.jpg"
                # print(result)
                with open(storeFilePath, "wb") as file:
                    file.write(img[2])
                    file.close()
        except Exception as e:
            pass
        #side Buttons
        self.submit = Button(self, width=8, text="Submit", fg='#FFFFFF',font=("Posterama", 15, 'bold'),
                                bg='#4361EE', activebackground='#FFFFFF', activeforeground='#4361EE',command=self.submit)
        self.submit.place(x=0.85 * self.winfo_screenwidth(),
                             y=0.1 * self.winfo_screenheight())

        self.cancel = Button(self, width=8, text="Cancel", fg='#FFFFFF', font=("Posterama", 15, 'bold'),
                             bg='#4361EE', activebackground='#FFFFFF', activeforeground='#4361EE', command=self.destroy)
        self.cancel.place(x=0.85 * self.winfo_screenwidth(),
                          y=0.15 * self.winfo_screenheight())

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
        self.personal_frame= self.main = Frame(second_frame, height=second_frame.winfo_screenheight(), width=0.9 * self.winfo_screenwidth(), bg='#FFFFFF')
        self.personal_frame.pack(side= TOP)

        self.academic_frame = self.main = Frame(second_frame, height=second_frame.winfo_screenheight(),width=0.9 * self.winfo_screenwidth(), bg='#4361EE')
        self.academic_frame.pack(side=TOP)

        self.document_frame = self.main = Canvas(second_frame, height=2.5*second_frame.winfo_screenheight(),width=0.9 * self.winfo_screenwidth(), bg='#FFFFFF')
        self.document_frame.pack(side=TOP)


        # personal Information

        self.personal = Label(self.personal_frame, text="Personal Information ", font=("Posterama", 45,'underline'), bg='#FFFFFF', fg='#4361EE')
        self.personal.place(x=0.05 * self.personal_frame.winfo_screenwidth(), y=0.05 * self.personal_frame.winfo_screenheight())

        self.personal2 = Label(self.personal_frame, text="Please, enter your Undermentioned Information ", font=("Posterama", 12,),bg='#FFFFFF', fg='#000000')
        self.personal2.place(x=0.05 * self.personal_frame.winfo_screenwidth(),y=0.13 * self.personal_frame.winfo_screenheight())

        self.first_name = ttk.Entry(self.personal_frame, width=25, font=("Posterama", 20))
        self.first_name.insert(0, result[2] )
        self.first_name.focus()
        self.first_name.place(x=0.05 * self.personal_frame.winfo_screenwidth(), y=0.2 * self.personal_frame.winfo_screenheight())

        self.last_name = ttk.Entry(self.personal_frame, width=25, font=("Posterama", 20))
        self.last_name.insert(0, result[3], )
        self.last_name.place(x=0.305 * self.personal_frame.winfo_screenwidth(), y=0.2 * self.personal_frame.winfo_screenheight())

        self.father_name = ttk.Entry(self.personal_frame, width=51, font=("Posterama", 20))
        self.father_name.insert(0, result[4], )
        self.father_name.place(x=0.05 * self.personal_frame.winfo_screenwidth(), y=0.27 * self.personal_frame.winfo_screenheight())

        self.mother_name = ttk.Entry(self.personal_frame, width=51, font=("Posterama", 20))
        self.mother_name.insert(0, result[5], )
        self.mother_name.place(x=0.05 * self.personal_frame.winfo_screenwidth(), y=0.34 * self.personal_frame.winfo_screenheight())

        self.dob = ttk.Entry(self.personal_frame, width=51, font=("Posterama", 20))
        self.dob.insert(0, result[6], )
        self.dob.place(x=0.05 * self.personal_frame.winfo_screenwidth(), y=0.41 * self.personal_frame.winfo_screenheight())

        field_list1=["Gender","Male","Female","Other"]
        self.gender = ttk.Combobox(self.personal_frame, values=field_list1, width=28, font=("Posterama", 20, ))
        self.gender.insert(0, result[7], )
        #self.gender.current(0)
        self.gender.place(x=0.05 * self.personal_frame.winfo_screenwidth(),
                       y=0.48 * self.personal_frame.winfo_screenheight())

        self.add1 = ttk.Entry(self.personal_frame, width=51, font=("Posterama", 20))
        self.add1.insert(0, result[8], )
        self.add1.place(x=0.05 * self.personal_frame.winfo_screenwidth(), y=0.55 * self.personal_frame.winfo_screenheight())

        self.add2 = ttk.Entry(self.personal_frame, width=51, font=("Posterama", 20))
        self.add2.insert(0, result[9], )
        self.add2.place(x=0.05 * self.personal_frame.winfo_screenwidth(),
                        y=0.62 * self.personal_frame.winfo_screenheight())

        self.city = ttk.Entry(self.personal_frame, width=25, font=("Posterama", 20))
        self.city.insert(0, result[10], )
        self.city.place(x=0.05 * self.personal_frame.winfo_screenwidth(),
                        y=0.69 * self.personal_frame.winfo_screenheight())

        self.district = ttk.Entry(self.personal_frame, width=25, font=("Posterama", 20))
        self.district.insert(0, result[11], )
        self.district.place(x=0.305 * self.personal_frame.winfo_screenwidth(),
                        y=0.69 * self.personal_frame.winfo_screenheight())

        self.state = ttk.Entry(self.personal_frame, width=25, font=("Posterama", 20))
        self.state.insert(0, result[12], )
        self.state.place(x=0.05 * self.personal_frame.winfo_screenwidth(),
                            y=0.76 * self.personal_frame.winfo_screenheight())

        self.pincode = ttk.Entry(self.personal_frame, width=25, font=("Posterama", 20))
        self.pincode.insert(0, result[13], )
        self.pincode.place(x=0.305 * self.personal_frame.winfo_screenwidth(),
                         y=0.76 * self.personal_frame.winfo_screenheight())

        field_list2 = ["General","SC / ST ","OBC","Others"]
        self.category = ttk.Combobox(self.personal_frame, values=field_list2, width=24, font=("Posterama", 20, ))
        self.category.insert(0, result[14], )
        self.category.place(x=0.05 * self.personal_frame.winfo_screenwidth(),
                           y=0.83 * self.personal_frame.winfo_screenheight())

        field_list3 = ["Hindu","Muslim","Sikhism","Christian","Jainism","Buddhism","Others"]
        self.religion = ttk.Combobox(self.personal_frame, values=field_list3, width=24, font=("Posterama", 20, ))
        self.religion.insert(0, result[15], )
        self.religion.place(x=0.305 * self.personal_frame.winfo_screenwidth(),
                            y=0.83 * self.personal_frame.winfo_screenheight())

        # academic information

        self.personal = Label(self.academic_frame, text="Academic & Economic Information ", font=("Posterama", 45, 'underline'),bg='#4361EE', fg='#FFFFFF')
        self.personal.place(x=0.05 * self.academic_frame.winfo_screenwidth(),y=0.05 * self.academic_frame.winfo_screenheight())

        self.personal2 = Label(self.academic_frame, text="Please, enter your Undermentioned Information ", font=("Posterama", 12,), bg='#4361EE', fg='#FFFFFF')
        self.personal2.place(x=0.05 * self.academic_frame.winfo_screenwidth(), y=0.13 * self.academic_frame.winfo_screenheight())

        self.foccupation = ttk.Entry(self.academic_frame, width=25, font=("Posterama", 20))
        self.foccupation.insert(0, result[16], )
        self.foccupation.place(x=0.05 * self.academic_frame.winfo_screenwidth(), y=0.2 * self.personal_frame.winfo_screenheight())

        self.moccupation = ttk.Entry(self.academic_frame, width=25, font=("Posterama", 20))
        self.moccupation.insert(0, result[17], )
        self.moccupation.place(x=0.305 * self.academic_frame.winfo_screenwidth(), y=0.2 * self.personal_frame.winfo_screenheight())

        self.fincome = ttk.Entry(self.academic_frame, width=25, font=("Posterama", 20))
        self.fincome.insert(0, result[18], )
        self.fincome.place(x=0.05 * self.academic_frame.winfo_screenwidth(), y=0.27 * self.personal_frame.winfo_screenheight())

        self.mincome = ttk.Entry(self.academic_frame, width=25, font=("Posterama", 20))
        self.mincome.insert(0, result[19], )
        self.mincome.place(x=0.305 * self.academic_frame.winfo_screenwidth(), y=0.27 * self.personal_frame.winfo_screenheight())

        self.personal = Label(self.academic_frame, text="10th Class Details",font=("Posterama", 25, 'bold underline'), bg='#4361EE', fg='#FFFFFF')
        self.personal.place(x=0.05 * self.academic_frame.winfo_screenwidth(), y=0.34 * self.academic_frame.winfo_screenheight())

        self.marks1_institute = ttk.Entry(self.academic_frame, width=51, font=("Posterama", 20))
        self.marks1_institute.insert(0, result[20], )
        self.marks1_institute.place(x=0.05 * self.personal_frame.winfo_screenwidth(), y=0.41 * self.personal_frame.winfo_screenheight())

        self.marks1_board = ttk.Entry(self.academic_frame, width=25, font=("Posterama", 20))
        self.marks1_board.insert(0, result[21], )
        self.marks1_board.place(x=0.05 * self.academic_frame.winfo_screenwidth(), y=0.48 * self.personal_frame.winfo_screenheight())

        self.marks1 = ttk.Entry(self.academic_frame, width=25, font=("Posterama", 20))
        self.marks1.insert(0, result[22], )
        self.marks1.place(x=0.305 * self.academic_frame.winfo_screenwidth(), y=0.48 * self.personal_frame.winfo_screenheight())

        self.personal = Label(self.academic_frame, text="12th Class / Diploma Details", font=("Posterama", 25, 'bold underline'),
                              bg='#4361EE', fg='#FFFFFF')
        self.personal.place(x=0.05 * self.academic_frame.winfo_screenwidth(), y=0.55 * self.academic_frame.winfo_screenheight())

        self.marks2_institute = ttk.Entry(self.academic_frame, width=51, font=("Posterama", 20))
        self.marks2_institute.insert(0, result[23], )
        self.marks2_institute.place(x=0.05 * self.personal_frame.winfo_screenwidth(), y=0.62 * self.personal_frame.winfo_screenheight())

        self.marks2_board = ttk.Entry(self.academic_frame, width=25, font=("Posterama", 20))
        self.marks2_board.insert(0, result[24], )
        self.marks2_board.place(x=0.05 * self.academic_frame.winfo_screenwidth(), y=0.69 * self.personal_frame.winfo_screenheight())

        self.marks2 = ttk.Entry(self.academic_frame, width=25, font=("Posterama", 20))
        self.marks2.insert(0, result[25], )
        self.marks2.place(x=0.305 * self.academic_frame.winfo_screenwidth(), y=0.69 * self.personal_frame.winfo_screenheight())

        self.personal = Label(self.academic_frame, text="Degree / Diploma Details (if Applicable)",font=("Posterama", 25, 'bold underline'), bg='#4361EE', fg='#FFFFFF')
        self.personal.place(x=0.05 * self.academic_frame.winfo_screenwidth(), y=0.76 * self.academic_frame.winfo_screenheight())

        aInteger = IntVar()
        def activateCheck():
            if aInteger.get() == 1:          #whenever checked
                self.marks3.config(state=NORMAL)
                self.marks3_institute.config(state=NORMAL)
                self.marks3_board.config(state=NORMAL)
                btn_list[5].config(state=NORMAL)
            elif aInteger.get() == 0:        #whenever unchecked
                self.marks3.config(state=DISABLED)
                self.marks3_institute.config(state=DISABLED)
                self.marks3_board.config(state=DISABLED)
                btn_list[5].config(state=DISABLED)

        self.chk = Checkbutton(self.academic_frame, variable=aInteger, command=activateCheck, bg ='#4361EE')
        self.chk.place(x=0.45 * self.academic_frame.winfo_screenwidth(), y=0.76 * self.academic_frame.winfo_screenheight())

        self.marks3_institute = ttk.Entry(self.academic_frame, width=51, font=("Posterama", 20))
        self.marks3_institute.insert(0, result[26], )
        self.marks3_institute.config(state=DISABLED)
        self.marks3_institute.place(x=0.05 * self.personal_frame.winfo_screenwidth(), y=0.82 * self.personal_frame.winfo_screenheight())

        self.marks3_board = ttk.Entry(self.academic_frame, width=25, font=("Posterama", 20))
        self.marks3_board.insert(0, result[27], )
        self.marks3_board.config(state=DISABLED)
        self.marks3_board.place(x=0.05 * self.academic_frame.winfo_screenwidth(), y=0.89 * self.personal_frame.winfo_screenheight())

        self.marks3 = ttk.Entry(self.academic_frame, width=25, font=("Posterama", 20))
        self.marks3.insert(0, result[28], )
        self.marks3.config(state=DISABLED)
        self.marks3.place(x=0.305 * self.academic_frame.winfo_screenwidth(), y=0.89 * self.personal_frame.winfo_screenheight())

    #  documents Uploading

        self.personal = Label(self.document_frame, text="Documents ", font=("Posterama", 45, 'underline'),
                              bg='#FFFFFF', fg='#4361EE')
        self.personal.place(x=0.05 * self.personal_frame.winfo_screenwidth(),
                            y=0.05 * self.personal_frame.winfo_screenheight())

        self.personal2 = Label(self.document_frame, text="Please, Upload your Undermentioned Documents ",
                               font=("Posterama", 12,), bg='#FFFFFF', fg='#000000')
        self.personal2.place(x=0.05 * self.personal_frame.winfo_screenwidth(),
                             y=0.13 * self.personal_frame.winfo_screenheight())

        field_list =["Photo","Signature","Date of Birth Proof","10th Certificate","12th Cetificate","Degree/Diploma","Character","Migration"]
        btn_list = []
        for i in field_list:
            btn_list.append(Button(self.document_frame, width=20, text=i, fg='#4361EE', font=("Posterama", 20, 'bold'),
                            bg='#FFFFFF', activebackground='#4361EE', activeforeground='#FFFFFF', command=lambda x=i:field_operation(x)))

        for i in range(0,len(field_list)):
            btn_list[i].place(x=0.1 * self.document_frame.winfo_screenwidth(), y=240*i+0.30 * self.document_frame.winfo_screenheight())

        btn_list[5].config(state=DISABLED)
        frame_list = []
        for i in range(0,8):
            frame_list.append(Label(self.document_frame, bg='#4361EE'))
        table_name = ["photo", "signature", "dob", "mark1", "mark2", "mark3", "character", "migration"]
        #If present adding pics to frame
        for i in range(0, len(table_name)):
            try:
                fln = "ImageOutputs/img{}{}.jpg".format(self.id,table_name[i])
                img = Image.open(fln)
                img.thumbnail((200, 200))  # for resizing
                img = ImageTk.PhotoImage(img)
                frame_list[i].configure(image=img)  # image
                frame_list[i].image = img  # image
            except Exception as e:
                pass

        for i in range(0,len(frame_list)):
            frame_list[i].place(x=0.45 * self.document_frame.winfo_screenwidth(), y=240*i+0.25 * self.document_frame.winfo_screenheight())
            self.document_frame.create_line(0.08 * self.document_frame.winfo_screenwidth(),
                                            240*i+0.225 * self.document_frame.winfo_screenheight(),
                                            0.65 * self.document_frame.winfo_screenwidth(),
                                            240*i+0.225* self.document_frame.winfo_screenheight())
            #canvas LINES
        self.document_frame.create_line(0.08 * self.document_frame.winfo_screenwidth(),
                                        0.225 * self.document_frame.winfo_screenheight(),
                                        0.08 * self.document_frame.winfo_screenwidth(),
                                        240 * len(frame_list) + 0.225 * self.document_frame.winfo_screenheight())
        self.document_frame.create_line(0.365 * self.document_frame.winfo_screenwidth(),
                                        0.225 * self.document_frame.winfo_screenheight(),
                                        0.365 * self.document_frame.winfo_screenwidth(),
                                        240 * len(frame_list) + 0.225 * self.document_frame.winfo_screenheight())
        self.document_frame.create_line(0.65 * self.document_frame.winfo_screenwidth(),
                                        0.225 * self.document_frame.winfo_screenheight(),
                                        0.65 * self.document_frame.winfo_screenwidth(),
                                        240 * len(frame_list) + 0.225 * self.document_frame.winfo_screenheight())
        self.document_frame.create_line(0.08 * self.document_frame.winfo_screenwidth(),
                                        240 * len(frame_list) + 0.225 * self.document_frame.winfo_screenheight(),
                                        0.65 * self.document_frame.winfo_screenwidth(),
                                        240 * len(frame_list) + 0.225 * self.document_frame.winfo_screenheight())
        def field_operation(x):
            frame_number=field_list.index(x)
            table_name = ["photo","signature","dob","mark1","mark2","mark3","character","migration"]
            #file Dialoge
            try:
                fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File",
                                             filetypes=(
                                             ("JPG file", "*.jpg"), ("PNG file", "*.png"), ("All Files", "*.*")))
                img = Image.open(fln)
                img.thumbnail((200, 200))  # for resizing
                img = ImageTk.PhotoImage(img)
                frame_list[frame_number].configure(image=img)  # image
                frame_list[frame_number].image = img  # image
            except Exception as e:
                messagebox.showerror("Error", "File Data type must be .jpeg or .png")

            try:
                query_delete = "DELETE FROM image1 where id ='{}' and name ='{}'".format(self.id,table_name[frame_number])
                cur.execute(query_delete)
                con.commit()
            except Exception as e:
                messagebox.showerror("Error", str(e))

            #file upload
            try:
                with open(fln, "rb") as file:
                    bData = file.read()
                sqlStatment = "insert into image1 (id,name,photo) values(?,?,?)"
                cur.execute(sqlStatment,(self.id,table_name[frame_number],bData))
                con.commit()
                messagebox.showinfo("Success", "Picture Uploaded")
            except Exception as e:
                messagebox.showerror("Error", "Couldn't Upload the file")

    def submit(self):
        id = self.id
        name = self.first_name.get()
        surname = self.last_name.get()
        fname = self.father_name.get()
        mname = self.mother_name.get()
        dob = self.dob.get()
        gender = self.gender.get()
        address1 = self.add1.get()
        address2 = self.add2.get()
        city = self.city.get()
        district = self.district.get()
        state = self.state.get()
        pincode = self.pincode.get()
        category = self.category.get()
        religion = self.religion.get()
        foccupation = self.foccupation.get()
        moccupation = self.moccupation.get()
        fincome = self.fincome.get()
        mincome = self.mincome.get()
        marks1_institute = self.marks1_institute.get()
        marks1_board = self.marks1_institute.get()
        marks1 = self.marks1.get()
        marks2_institute = self.marks2_institute.get()
        marks2_board = self.marks2_institute.get()
        marks2 = self.marks2.get()
        marks3_institute = self.marks3_institute.get()
        marks3_board = self.marks3_institute.get()
        marks3 = self.marks3.get()

        query_1 = "update student set name = '{}', surname = '{}', fname= '{}', mname='{}', dob = '{}', gender ='{}' where id = {}".format(name,surname,fname,mname,dob,gender,id)
        query_2 = "update student set address1 = '{}', address2 = '{}', city = '{}', district ='{}', state = '{}', pincode ='{}' where id = {}".format(
            address1, address2, city, district, state, pincode, id)
        query_3 = "update student set category = '{}', religion = '{}', foccupation = '{}', moccupation ='{}', fincome = '{}', mincome ='{}' where id = {}".format(
            category, religion, foccupation, moccupation, fincome, mincome, id)
        query_4 = "update student set marks1_institute = '{}', marks1_board = '{}', marks1 = '{}' where id = {}".format(
            marks1_institute, marks1_board, marks1, id)
        query_5 = "update student set marks1_institute = '{}', marks1_board = '{}', marks1 = '{}' where id = {}".format(
            marks2_institute, marks2_board, marks2, id)
        query_6 = "update student set marks1_institute = '{}', marks1_board = '{}', marks1 = '{}' where id = {}".format(
            marks3_institute, marks3_board, marks3, id)

        try:
            cur.execute(query_1)
            cur.execute(query_2)
            cur.execute(query_3)
            cur.execute(query_4)
            cur.execute(query_5)
            cur.execute(query_6)
            con.commit()
            messagebox.showinfo("Success", "Contact updated")

        except Exception as e:
            messagebox.showerror("Error", str(e))

