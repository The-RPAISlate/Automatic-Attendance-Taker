import pandas as pd
from glob import glob
import os
import tkinter
import csv
import tkinter as tk
from tkinter import *

def subjectchoose(text_to_speech,is_on):
    def calculate_attendance():
        Subject = tx.get()
        if Subject=="":
            t='Please enter the subject name.'
            text_to_speech(t)
        os.chdir(
            f"C:\\Users\\sudha\\Desktop\\Attendance-Management-system-using-face-recognition-master\\Attandance\\{Subject}"
        )
        filenames = glob(
            f"C:\\Users\\sudha\\Desktop\\Attendance-Management-system-using-face-recognition-master\\Attandance\\{Subject}\\{Subject}*.csv"
        )
        df = [pd.read_csv(f) for f in filenames]
        newdf = df[0]
        for i in range(1, len(df)):
            newdf = newdf.merge(df[i], how="outer")
        newdf.fillna(0, inplace=True)
        newdf["Attendance"] = 0
        for i in range(len(newdf)):
            newdf["Attendance"].iloc[i] = str(int(round(newdf.iloc[i, 2:-1].mean() * 100)))+'%'
            #newdf.sort_values(by=['Enrollment'],inplace=True)
        newdf.to_csv("attendance.csv", index=False)

        root = tkinter.Tk()
        root.title("Attendance of "+Subject)
        root.configure(background="black")
        cs = f"C:\\Users\\sudha\\Desktop\\Attendance-Management-system-using-face-recognition-master\\Attandance\\{Subject}\\attendance.csv"
        with open(cs) as file:
            reader = csv.reader(file)
            r = 0

            for col in reader:
                c = 0
                for row in col:

                    label = tkinter.Label(
                        root,
                        width=10,
                        height=1,
                        fg="yellow",
                        font=("times", 15, " bold "),
                        bg="black",
                        text=row,
                        relief=tkinter.RIDGE,
                    )
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        root.mainloop()
        print(newdf)

    subject = Tk()
    # windo.iconbitmap("AMS.ico")
    subject.title("Subject...")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="light grey")
    titl = tk.Label(subject, bg="black",  bd=10, font=("arial", 30))
    titl.pack(fill=X)
    # l1 = tk.Label(subject, image=subject_logo1, bg="black",)
    # l1.place(x=100, y=10)
    titl_view_attendance = tk.Label(
        subject,
        text="Subject",
        bg="black",
        fg="dark orange",
        font=("arial", 25),
    )
    titl_view_attendance.place(x=150, y=12)
    
    titl1_view_attendance = tk.Label(
        subject,
        text="of",
        bg="black",
        fg="white",
        font=("arial", 25),
    )
    titl1_view_attendance.place(x=266, y=12)
    
    titl2_view_attendance = tk.Label(
        subject,
        text="Attendance",
        bg="black",
        fg="green",
        font=("arial", 25),
    )
    titl2_view_attendance.place(x=302, y=12)

    def Attf():
        sub = tx.get()
        if sub == "":
            t="Please enter the subject name!!!"
            text_to_speech(t)
        else:
            os.startfile(
            f"C:\\Users\\sudha\\Desktop\\Attendance-Management-system-using-face-recognition-master\\Attandance\\{sub}"
            )


    attf = tk.Button(
        subject,
        text="Check Sheets",
        command=Attf,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="green",
        height=2,
        width=10,
        # relief=RIDGE,
        borderwidth=0
    )
    attf.place(x=360, y=170)

    sub = tk.Label(
        subject,
        text="Enter Subject",
        width=10,
        height=2,
        bg="black",
        fg="dark orange",
        bd=5,
        # relief=RIDGE,
        font=("times new roman", 15),
        borderwidth=0
    )
    sub.place(x=50, y=100)

    tx = tk.Entry(
        subject,
        width=15,
        bd=5,
        bg="grey",
        fg="red",
        relief="groove",
        font=("times", 30, "bold"),
        borderwidth=0
    )
    tx.place(x=190, y=100)

    fill_a = tk.Button(
        subject,
        text="View Attendance",
        command=calculate_attendance,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="white",
        height=2,
        width=12,
        # relief=RIDGE,
        borderwidth=0
    )
    fill_a.place(x=195, y=170)
    
    
    def toggle(is_on):
        if(is_on):
            fill_a = tk.Button(
            subject,
            text="उपस्थिति देखें",
            command=calculate_attendance,
            bd=7,
            font=("times new roman", 15),
            bg="black",
            fg="white",
            height=2,
            width=12,
        # relief=RIDGE,
            borderwidth=0
            )
            fill_a.place(x=195, y=170)
            
            sub = tk.Label(
            subject,
            text="विषय लिखिए",
            width=10,
            height=2,
            bg="black",
            fg="dark orange",
            bd=5,
            # relief=RIDGE,
            font=("times new roman", 15),
            borderwidth=0
            )
            sub.place(x=50, y=100)

            attf = tk.Button(
            subject,
            text="पत्रक देखिये",
            command=Attf,
            bd=7,
            font=("times new roman", 15),
            bg="black",
            fg="green",
            height=2,
            width=10,
            # relief=RIDGE,
            borderwidth=0
            )
            attf.place(x=360, y=170)
            
            
        else:
            fill_a = tk.Button(
            subject,
            text="View Attendance",
            command=calculate_attendance,
            bd=7,
            font=("times new roman", 15),
            bg="black",
            fg="white",
            height=2,
            width=12,
        # relief=RIDGE,
            borderwidth=0
            )
            fill_a.place(x=195, y=170)
            
            sub = tk.Label(
            subject,
            text="Enter Subject",
            width=10,
            height=2,
            bg="black",
            fg="dark orange",
            bd=5,
            # relief=RIDGE,
            font=("times new roman", 15),
            borderwidth=0
            )
            sub.place(x=50, y=100)
    
            attf = tk.Button(
            subject,
            text="Check Sheets",
            command=Attf,
            bd=7,
            font=("times new roman", 15),
            bg="black",
            fg="green",
            height=2,
            width=10,
            # relief=RIDGE,
            borderwidth=0
            )
            attf.place(x=360, y=170)
            
            
    toggle(is_on)
            
    subject.mainloop()
