from cgitb import text
import tkinter as tk
from tkinter import *
import os, cv2
# from tkinter import _Relief
from turtle import width
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3
import PIL.Image
import PIL.ImageTk
    
# project module
import show_attendance   
import takeImage   
import trainImage   
import automaticAttedance   
from fnmatch import translate   
from googletrans import Translator   
   
   
def text_to_speech(user_text):   
    engine = pyttsx3.init()   
    engine.say(user_text)   
    engine.runAndWait()   
   
   
haarcasecade_path = "haarcascade_frontalface_default.xml"   
trainimagelabel_path = (   
    "TrainingImageLabel\Trainner.yml"
)
trainimage_path = "TrainingImage"
studentdetail_path = (
    "StudentDetails\studentdetails.csv"
)
attendance_path = "Attandance"
schoolName = ""
# schoolName = "St Mary's Convent Sr. Sec School"

window = Tk()
window.title("Face recognizer")
window.geometry("1280x720")
window.resizable(0, 0)
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background="light grey")

global take_attendance_button
take_attendance_button=False
# to destroy screen
def del_sc1():
    sc1.destroy()


# error message for name and no
def err_screen():
    
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="black")
    sc1.resizable(0, 0)
    
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="red",
        bg="black",
        font=("times", 20, " bold "),
    ).pack()
    
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="red",
        bg="black",
        width=9,
        height=1,
        activebackground="Red",
        font=("times", 20, " bold "),
    ).place(x=110, y=50)


def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True

##################################TRANSLATION SWITCH###########################################


is_on=False

def switch():
    global Edit
    # global ImageUI
    
    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")
        
    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )
        
    def modify():
        ChangeName=edit_name_input.get()
        ChangeRoll=edit_roll_input.get()
        
        folder_path = "TrainingImage"
        dir_list = os.listdir(folder_path)
        # print(dir_list)
        if(len(dir_list)!=0):
            final_list=[]
            
            for i in dir_list:
                final_list.append(i.split('_'))

            delete_folder_name="TrainingImage/"

            for i in final_list:
                if(i[0]==ChangeRoll and i[1]==ChangeName):
                    delete_folder_name+=i[0] + "_" +i[1]

            shutil.rmtree(delete_folder_name)
##############################SHEET###############################
        df= pd.read_csv("StudentDetails/studentdetails.csv")

        for i in range(0,df.shape[0]):
            print(type(df["Enrollment"][i]))
            if(df["Enrollment"][i]==int(ChangeRoll) and df["Name"][i]==ChangeName):
                df=df.drop(i,axis=0)

        df.to_csv("StudentDetails/studentdetails.csv",index=False)
    
    global is_on
    
    if(is_on):
        translation_switch.config(image = off)
        is_on=False
        
        r = tk.Button(
        window,
        text="Register Student",
        command=TakeImageUI,
        bd=10,
        font=("times new roman", 16),
        bg="black",
        fg="dark orange",
        height=2,
        width=19,
        borderwidth=0,
                )
        r.place(x=100, y=520)
        
        r = tk.Button(
        window,
        text="Take Attendance",
        command=automatic_attedance,
        bd=10,
        font=("times new roman", 16),
        bg="black",
        fg="white",
        height=2,
        width=19,
        borderwidth=0
        )
        r.place(x=550, y=520)
        
        r = tk.Button(
        window,
        text="View Attendance",
        command=view_attendance,
        bd=10,
        font=("times new roman", 16),
        bg="black",
        fg="green",
        height=2,
        width=19,
        borderwidth=0
    
        )
        r.place(x=980, y=520)
        
        r = tk.Button(
        window,
        text="EXIT",
        bd=10,
        command=quit,
        font=("times new roman", 16),
        bg="white",
        fg="red",
        height=2,
        width=19,
        borderwidth=0,
        highlightbackground="black",
        highlightthickness=2
        )
        r.pack()
        r.place(x=550, y=630)
        
        
        
    else: 
        translation_switch.config(image = on)
        is_on=True
        
        r = tk.Button(
        window,
        text="छात्र पंजीकृत करें",
        command=TakeImageUI,
        bd=10,
        font=("times new roman", 16),
        bg="black",
        fg="dark orange",
        height=2,
        width=19,
        borderwidth=0,
        )
        r.place(x=100, y=520)
        
        #Take Attendance
        
        r = tk.Button(
        window,
        text="उपस्थिति लें",
        command=automatic_attedance,
        bd=10,
        font=("times new roman", 16),
        bg="black",
        fg="white",
        height=2,
        width=19,
        borderwidth=0
        )
        r.place(x=550, y=520)
        
        # View Attendance
        
        r = tk.Button(
        window,
        text="उपस्थिति देखें",
        command=view_attendance,
        bd=10,
        font=("times new roman", 16),
        bg="black",
        fg="green",
        height=2,
        width=19,
        borderwidth=0
    
        )
        r.place(x=980, y=520)
        
        r = tk.Button(
        window,
        text="प्रस्थान",
        bd=10,
        command=quit,
        font=("times new roman", 16),
        bg="white",
        fg="red",
        height=2,
        width=17,
        borderwidth=0,
        highlightbackground="black",
        highlightthickness=2
        )
        r.pack()
        r.place(x=550, y=630)
        

translator = Translator()

is_on = False
on = PhotoImage(file = "UI_Image\on.png")
off = PhotoImage(file = "UI_Image\off.png")



translation_switch = Button(window, image = off, bd = 0,
                   command = switch)

translation_switch.pack(pady = 50)
translation_switch.place(x=1115,y=100)

##################################TRANSLATION SWITCH###########################################

logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 47), Image.ANTIALIAS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="black", relief="flat", bd=10, font=("arial", 35))
titl.pack(fill=X)
# l1 = tk.Label(window, image=logo1, bg="black",)
# l1.place(x=430, y=10)

titl = tk.Label(
   
    window, text = "Automatic", bg = "black", fg = "dark orange", font=("arial", 28),borderwidth=0
)
titl.place(x=476, y=12)

titl2 = tk.Label(
    window, text = "Attendance", bg = "black", fg = "white", font=("arial", 27),
)
titl2.place(x=645,y=12)

titl3 = tk.Label(
    window, text = "Collector", bg = "black", fg = "green", font=("arial", 27),
)
titl3.place(x=832,y=12)

# For DElete Window

#School Name 
a = tk.Label(
    window,
    # text="Welcome to the Face Recognition Based\nAttendance Management System",
    text= schoolName + "\nSit straight and face the camera",
    bg="light grey",
    fg="black",
    bd=10,
    font=("arial", 30),
)
a.pack()

ri = Image.open("UI_Image/register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=100, y=270)



im = PIL.Image.open("UI_Image/attendance.png")
photo = PIL.ImageTk.PhotoImage(im)
label2 = Label(window, image=photo)
label2.image = a
label2.place(x=980, y=270)

vi = Image.open("UI_Image/verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=550, y=270)



def TakeImageUI():
    global edit_name_input 
    global ImageUI
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="light grey")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="black",  bd=10, font=("arial", 35))
    titl.pack(fill=X)
    
    
    titl_newstudent = tk.Label(
        ImageUI, text="Register", bg="black", fg="dark orange", font=("arial", 30),borderwidth=0,relief="flat"
    )
    titl_newstudent.place(x=250, y=12)
    
    titl1_newstudent = tk.Label(
        ImageUI, text="Your", bg="black", fg="white", font=("arial", 30),borderwidth=0,relief="flat"
    )
    titl1_newstudent.place(x=405, y=12)
    
    titl2_newstudent = tk.Label(
        ImageUI, text="Face", bg="black", fg="green", font=("arial", 30),borderwidth=0,relief="flat"
    )
    titl2_newstudent.place(x=500, y=12)

    # heading
    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="light grey",
        fg="black",
        bd=10,
        font=("arial", 24),
    )
    a.place(x=280, y=75)

    # ER no
    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="dark orange",
        borderwidth=0,

    )
    lbl1.place(x=120, y=130)
    
    global txt1,txt2
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="grey",
        fg="red",
        # relief=RIDGE,
        font=("times", 25, "bold"),
        borderwidth=1,
        relief="groove"
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        # bg="black",
        # fg="red",
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="white",
        borderwidth=0,
    )
    lbl2.place(x=120, y=200)
    
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="grey",
        fg="red",
        relief="groove",
        font=("times", 25, "bold"),
        borderwidth=1
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        # bg="black",
        # fg="red",
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="green",
        borderwidth=0,
    )
    lbl3.place(x=120, y=270)
    
    global message
    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="grey",
        fg="red",
        relief="groove",
        font=("times", 12, "bold"),
        borderwidth=1
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # take Image button
    # image
    

    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=0,
        font=("times new roman", 16),
        bg="black",
        fg="red",
        height=2,
        width=12,
        # relief=RIDGE,
        borderwidth=0
    )
    takeImg.place(x=121, y=350)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    # train Image function call
    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("times new roman", 16),
        bg="black",
        fg="red",
        height=2,
        width=12,
        borderwidth=0
        # relief=RIDGE,
    )
    trainImg.place(x=300, y=350)
    
    #######################################EDIT#############################
    EditImg = tk.Button(
        ImageUI,
        text="Delete",
        command=edit,
        bd=10,
        font=("times new roman", 16),
        bg="black",
        fg="red",
        height=2,
        width=12,
        borderwidth=0
        # relief=RIDGE,
    )
    EditImg.place(x=470, y=350)
    
    def toggle_new_student(is_on):
        if(is_on):
            takeImg = tk.Button(
            ImageUI,
            text="छवि लें",
            command=take_image,
            bd=0,
            font=("times new roman", 16),
            bg="black",
            fg="red",
            height=2,
            width=12,
            # relief=RIDGE,
            borderwidth=0
            )
            takeImg.place(x=121, y=350)
            
            trainImg = tk.Button(
            ImageUI,
            text="रजिस्टर करें",
            command=train_image,
            bd=10,
            font=("times new roman", 16),
            bg="black",
            fg="red",
            height=2,
            width=12,
            borderwidth=0
            # relief=RIDGE,
            )
            trainImg.place(x=300, y=350)
            
            Del = tk.Button(
            ImageUI,
            text="मिटाये",
            command=edit,
            bd=0,
            font=("times new roman", 16),
            bg="black",
            fg="red",
            height=2,
            width=12,
            # relief=RIDGE,
            borderwidth=0
            )
            Del.place(x=470, y=350)
            
            
            edit_roll = tk.Label(
            ImageUI,
            text="अनुक्रमांक",
            width=10,
            height=2,
        
            bd=5,
            # relief=RIDGE,
            font=("times new roman", 12),
            bg="black",
            fg="dark orange",
            borderwidth=0,
            )
            edit_roll.place(x=120, y=130)
            
            edit_name = tk.Label(
            ImageUI,
            text="नाम",
            width=10,
            height=2,
            # bg="black",
            # fg="red",
            bd=5,
            # relief=RIDGE,
            font=("times new roman", 12),
            bg="black",
            fg="white",
            borderwidth=0,
            )
            edit_name.place(x=120, y=200)
            
            lbl3 = tk.Label(
            ImageUI,
            text="अधिसूचना",
            width=10,
            height=2,
            # bg="black",
            # fg="red",
            bd=5,
            # relief=RIDGE,
            font=("times new roman", 12),
            bg="black",
            fg="green",
            borderwidth=0,
                )
            lbl3.place(x=120, y=270)
            
            Del = tk.Button(
            ImageUI,
            text="मिटाये", 
            command=edit,
            bd=0,
            font=("times new roman", 16),
            bg="black",
            fg="red",
            height=2,
            width=12,
            # relief=RIDGE,
            borderwidth=0
            )
            Del.place(x=470, y=350)
            
        else:
            takeImg = tk.Button(
            ImageUI,
            text="Take Image",
            command=take_image,
            bd=0,
            font=("times new roman", 16),
            bg="black",
            fg="red",
            height=2,
            width=12,
            # relief=RIDGE,
            borderwidth=0
            )
            takeImg.place(x=121, y=350)
            
            trainImg = tk.Button(
            ImageUI,
            text="Train Image",
            command=train_image,
            bd=10,
            font=("times new roman", 16),
            bg="black",
            fg="red",
            height=2,
            width=12,
            borderwidth=0
            # relief=RIDGE,
            )
            trainImg.place(x=300, y=350)
            
            lbl1 = tk.Label(
            ImageUI,
            text="Enrollment No",
            width=10,
            height=2,
            
            bd=5,
            # relief=RIDGE,
            font=("times new roman", 12),
            bg="black",
            fg="dark orange",
            borderwidth=0,

            )
            lbl1.place(x=120, y=130)
            
            lbl2 = tk.Label(
            ImageUI,
            text="Name",
            width=10,
            height=2,
            # bg="black",
            # fg="red",
            bd=5,
            # relief=RIDGE,
            font=("times new roman", 12),
            bg="black",
            fg="white",
            borderwidth=0,
            )
            lbl2.place(x=120, y=200)
            
            lbl3 = tk.Label(
            ImageUI,
            text="Notification",
            width=10,
            height=2,
            # bg="black",
            # fg="red",
            bd=5,
            # relief=RIDGE,
            font=("times new roman", 12),
            bg="black",
            fg="green",
            borderwidth=0,
            )
            lbl3.place(x=120, y=270)
            
            Del = tk.Button(
            ImageUI,
            text="Delete",
            command=edit,
            bd=0,
            font=("times new roman", 16),
            bg="black",
            fg="red",
            height=2,
            width=12,
            # relief=RIDGE,
            borderwidth=0
            )
            Del.place(x=470, y=350)
                    
    toggle_new_student(is_on)
    

 
# global Edit             
def edit():
    Edit = Tk()
    Edit.title("Take Student Image..")
    Edit.geometry("780x480")
    Edit.configure(background="light grey")
    Edit.resizable(0, 0)
    titl = tk.Label(Edit, bg="black", relief="flat", bd=10, font=("arial", 35))
    titl.pack(fill=X)
    titl = tk.Label(
   
    Edit, text = "Delete", bg = "black", fg = "dark orange", font=("arial", 28),borderwidth=0
    )
    titl.place(x=210, y=12)

    titl2 = tk.Label(
        Edit, text = "Student", bg = "black", fg = "white", font=("arial", 27),
    )
    titl2.place(x=320,y=12)

    titl3 = tk.Label(
        Edit, text = "Entry", bg = "black", fg = "green", font=("arial", 27),
    )
    titl3.place(x=454,y=12)
    
    def modify():
        ChangeName=edit_name_input.get()
        ChangeRoll=edit_roll_input.get()
        
        folder_path = "TrainingImage"
        dir_list = os.listdir(folder_path)
        # print(dir_list)
        if(len(dir_list)!=0):
            final_list=[]
            
            for i in dir_list:
                final_list.append(i.split('_'))

            delete_folder_name="TrainingImage/"

            for i in final_list:
                if(i[0]==ChangeRoll and i[1]==ChangeName):
                    delete_folder_name+=i[0] + "_" +i[1]

            shutil.rmtree(delete_folder_name)
##############################SHEET###############################
        df= pd.read_csv("StudentDetails/studentdetails.csv")

        for i in range(0,df.shape[0]):
            print(type(df["Enrollment"][i]))
            if(df["Enrollment"][i]==int(ChangeRoll) and df["Name"][i]==ChangeName):
                df=df.drop(i,axis=0)

        df.to_csv("StudentDetails/studentdetails.csv",index=False)
    
    
    edit_name = tk.Label(
        Edit,
        text="Name",
        width=10,
        height=2,
        # bg="black",
        # fg="red",
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="dark orange",
        borderwidth=0,
    )
    edit_name.place(x=120, y=170)
    
    global edit_name_input
    edit_name_input = tk.Entry(
        Edit,
        width=17,
        bd=5,
        bg="grey",
        fg="red",
        relief="groove",
        font=("times", 25, "bold"),
        borderwidth=1
    )
    edit_name_input.place(x=250, y=170)

    edit_roll = tk.Label(
        Edit,
        text="Enrollment No",
        width=10,
        height=2,
        # bg="black",
        # fg="red",
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 12),
        bg="black",
        fg="white",
        borderwidth=0,
    )
    edit_roll.place(x=120, y=270)
    
    global edit_roll_input
    
    edit_roll_input = tk.Entry(
        Edit,
        width=17,
        bd=5,
        bg="grey",
        fg="red",
        relief="groove",
        font=("times", 25, "bold"),
        borderwidth=1
    )
    edit_roll_input.place(x=250, y=270)
    
    Submit = tk.Button(
        Edit,
        text="Submit",
        command=modify,
        bd=10,
        font=("times new roman", 16),
        bg="black",
        fg="red",
        height=2,
        width=12,
        borderwidth=0
        # relief=RIDGE,
    )
    Submit.place(x=270, y=350)
    
   
r = tk.Button(
    window,
    text="Register Student",
    command=TakeImageUI,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="dark orange",
    height=2,
    width=19,
    borderwidth=0,
)
r.place(x=100, y=520)


print(is_on)


def automatic_attedance():
    take_attendance_button=True
    automaticAttedance.subjectChoose(text_to_speech,is_on)
    


r = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attedance,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="white",
    height=2,
    width=19,
    borderwidth=0
)
r.place(x=550, y=520)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech,is_on)


r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="green",
    height=2,
    width=19,
    borderwidth=0
    
)
r.place(x=980, y=520)

r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("times new roman", 16),
    bg="white",
    fg="red",
    height=2,
    width=19,
    borderwidth=0,
    highlightbackground="black",
    highlightthickness=2
)
r.pack()
r.place(x=550, y=630)

window.mainloop()
