from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import datetime
import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox
import tkinter as tk
import webbrowser
from tkinter import messagebox
from tkcalendar import DateEntry 

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt

from tkinter import Tk, PhotoImage
import tkinter as tk
from tkinter import messagebox, ttk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from backend import *
from MYSQL import *
#from Home import *
#from Login import *





background="#f0ddd5"
framebg="#62a7ff"
framefg="#fefbfb"

root= tk.Tk()
root.title("Heart Attack Prediction System")
root.geometry("1450x730+60+80")
root.resizable(True,True)
root.config(bg=background)




########## def analysis <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,
from datetime import datetime, date
def analysis():
    global prediction
    
    name=Name.get()
    D1=Date.get()

    birth_date = datetime.strptime(D1, "%d/%m/%Y").date()
    today = date.today()
    A = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

#     today=datetime.date.today()
#     A=today.year-DOB.get()

    try:
         B=selection()
    except:
         messagebox.showerror("missing","Please select gender!!")
         return
    
    
    try:
         F=selection2()
    except:
         messagebox.showerror("missing","Please select fbs!!")
         return
    
    
    try:
         I=selection3()
    except:
         messagebox.showerror("missing","Please select exang!!")
         return
    
    
    try:
         C=int(selection4())
    except:
         messagebox.showerror("missing","Please select cp!!")
         return
    
    try:
         K=int(selection5())
    except:
         messagebox.showerror("missing","Please select slope!!")
         return
    
    try:
         G=int(restecg_comobobox.get())
    except:
         messagebox.showerror("missing","Please select restecg!!")
         return
    
    try:
         L=int(ca_comobobox.get())
    except:
         messagebox.showerror("missing","Please select ca!!")
         return
    
    try:
         M=int(thal_comobobox.get())
    except:
         messagebox.showerror("missing","Please select thal!!")
         return


    try:
         D=int(trestbps.get()) 
         E=int(chol.get())
         H=int(thalach.get())
         J=int(oldpeak.get())

    except:
         messagebox.showerror("missing data","Few missing data entry!!")
         return
    

    

     ### lets check all are working or not
    print("A is age:", A)
    print("B is gender:",B)
    print("C is cp:",C)
    print("D is trestbps:",D)
    print("E is chol",E)
    print("F is fbs:",F)
    print("G is restecg",G)
    print("H is thalach",H)
    print("I is Exang:",I)
    print("J is oldpeak:",J)
    print("K is slop:",K)
    print("L is ca:",L)
    print("M is thal:",M)

    #### First graph ###############
    f = Figure(figsize=(5,5),dpi=100)
    a = f.add_subplot(111)
    a.plot(["Sex","fbs","exang"])
    canvas = FigureCanvasTkAgg(f)
    canvas .get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas._tkcanvas.place(width=250,height=250,x=600,y=240)


    #### second graph #############
    f2 = Figure(figsize=(5,5),dpi=100)
    a2 = f2.add_subplot(111)
    a2.plot(["age","trestbps","chol","thalach"],[A,D,E,H])
    canvas2 = FigureCanvasTkAgg(f2)
    canvas2.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas2._tkcanvas.place(width=250,height=250,x=860,y=240)


    #### Third graph #############
    f3 = Figure(figsize=(5,5),dpi=100)
    a3 = f3.add_subplot(111)
    a3.plot(["oldpeak","resticg","cp"],[J,G,C])
    canvas3 = FigureCanvasTkAgg(f3)
    canvas3.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas3._tkcanvas.place(width=250,height=250,x=600,y=470)

    #### Fourth graph #############
    f4 = Figure(figsize=(5,5),dpi=100)
    a4 = f4.add_subplot(111)
    a4.plot(["slope","ca","thal"],[K,L,M])
    canvas4 = FigureCanvasTkAgg(f4)
    canvas4.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas4._tkcanvas.place(width=250,height=250,x=860,y=470)


    ########### input data
    
    input_data=(A,B,C,D,E,F,G,H,I,J,K,L,M)

    input_data_as_numpy_array=np.asanyarray(input_data)

    #reshape the numpy array as we are predicting for only on instance
    input_data_reshape=input_data_as_numpy_array.reshape(1,-1)

    prediction= model.predict(input_data_reshape)
    print(prediction[0])

    if (prediction[0]==0):
     print("The Person does not have a Heart disease")
     report.config(text=f"Report:{0}",fg="#8dc63f")
     report1.config(text=f"{name},you do not have a heart disease")

    else:
     print("The Person has Heart disease")
     report.config(text=f"Report:{1}",fg="#ed1c24")
     report1.config(text=f"{name},you have a heart disease")
     show_doctors()
'''
import tkinter as tk
import webbrowser
from tkinter import messagebox
'''
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import mysql.connector
from tkinter import Toplevel


# Function to display recommended doctors in a table format
def show_doctors():
    doctor_list = [
        {"name": "Dr. A Sharma", "specialization": "Cardiologist", "contact": "123-456-7890", "email": "dr.asharma@gmail.com", "location": "New Delhi, India", "experience": "10 years", "rating": "4.5/5"},
        {"name": "Dr. B Verma", "specialization": "Heart Specialist", "contact": "987-654-3210", "email": "dr.bverma@gmail.com", "location": "Mumbai, India", "experience": "8 years", "rating": "4.7/5"},
        {"name": "Dr. C Mehta", "specialization": "Cardiac Surgeon", "contact": "456-789-1234", "email": "dr.cmehta@gmail.com", "location": "Bangalore, India", "experience": "15 years", "rating": "4.8/5"},
        {"name": "Dr. D Kapoor", "specialization": "Interventional Cardiologist", "contact": "555-234-5678", "email": "dr.dkapoor@gmail.com", "location": "Chennai, India", "experience": "12 years", "rating": "4.6/5"},
        {"name": "Dr. E Reddy", "specialization": "Heart Failure Specialist", "contact": "777-654-3210", "email": "dr.ereaddy@gmail.com", "location": "Hyderabad, India", "experience": "9 years", "rating": "4.5/5"},
        {"name": "Dr. F Gupta", "specialization": "Cardiac Electrophysiologist", "contact": "666-789-1234", "email": "dr.fgupta@gmail.com", "location": "Pune, India", "experience": "11 years", "rating": "4.7/5"},
        {"name": "Dr. G Saxena", "specialization": "Pediatric Cardiologist", "contact": "888-123-4567", "email": "dr.gsaxena@gmail.com", "location": "Kolkata, India", "experience": "13 years", "rating": "4.9/5"},
        {"name": "Dr. H Mishra", "specialization": "Preventive Cardiologist", "contact": "999-456-7890", "email": "dr.hmishra@gmail.com", "location": "Ahmedabad, India", "experience": "10 years", "rating": "4.6/5"},
    ]

    # Create doctor window
    doctor_window = tk.Toplevel(root)
    doctor_window.title("Recommended Doctors")
    doctor_window.geometry("900x400")
    doctor_window.configure(bg="#f4f4f4")

    # Title Label
    title_label = tk.Label(doctor_window, text="Recommended Cardiologists", font=("Arial", 14, "bold"), bg="#f4f4f4", fg="#333")
    title_label.pack(pady=10)

    # Table (Treeview)
    columns = ("Name", "Specialization", "Experience", "Rating", "Location", "Contact", "Email")
    
    tree = ttk.Treeview(doctor_window, columns=columns, show="headings", height=8)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    # Define Column Headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")

    # Insert Data into Table
    for doc in doctor_list:
        tree.insert("", "end", values=(doc['name'], doc['specialization'], doc['experience'], doc['rating'], doc['location'], doc['contact'], doc['email']))

    # Scrollbar
    scrollbar = ttk.Scrollbar(doctor_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Copy Contact Button
    def copy_selected():
        selected_item = tree.selection()
        if selected_item:
            doc_info = tree.item(selected_item, "values")
            contact_info = f"Phone: {doc_info[5]} | Email: {doc_info[6]}"
            root.clipboard_clear()
            root.clipboard_append(contact_info)
            root.update()
            messagebox.showinfo("Copied", f"Contact details copied:\n{contact_info}")
        else:
            messagebox.showwarning("Selection Error", "Please select a doctor to copy contact details.")

    copy_button = tk.Button(doctor_window, text="Copy Contact", font=("Arial", 10, "bold"), bg="#62a7ff", fg="white", padx=10, pady=5, command=copy_selected)
    copy_button.pack(pady=5)

    # Open Email Function
    def open_selected_email():
        selected_item = tree.selection()
        if selected_item:
            doc_info = tree.item(selected_item, "values")
            open_email(doc_info[6])
        else:
            messagebox.showwarning("Selection Error", "Please select a doctor to send an email.")

    email_button = tk.Button(doctor_window, text="Send Email", font=("Arial", 10, "bold"), bg="#28a745", fg="white", padx=10, pady=5, command=open_selected_email)
    email_button.pack(pady=5)

    # Close Button
    tk.Button(doctor_window, text="Close", command=doctor_window.destroy, bg="red", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5).pack(pady=5)

# Function to open Gmail with a prefilled email
def open_email(email):
    subject = "Appointment Request"
    body = "Dear Doctor,\n\nI would like to schedule an appointment with you.\n\nBest regards."
    gmail_url = f"https://mail.google.com/mail/?view=cm&to={email}&su={subject}&body={body}"
    webbrowser.open(gmail_url)

# Open Doctor List Button
doctor_button = tk.Button(root, text="Show Recommended Doctors", font=("Arial", 14, "bold"), bg="#df2d4b", fg="white", command=show_doctors)
doctor_button.pack(pady=50)


#### info window (operated by info button)<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def Info():
     Icon_window=Toplevel(root)
     Icon_window.title("Info")
     Icon_window.geometry("700x600+400+100")

     #icon_image
     icon_image=PhotoImage(file="Image/info.png")
     Icon_window.iconphoto(False,icon_image)

     #heading
     Label(Icon_window,text="Information related to dataset",font="robat 19 bold").pack(padx=20,pady=21)


     #info
     Label(Icon_window,text="age - age in years",font="arial 11").place(x=20,y=100)
     Label(Icon_window,text="sex - sex (1 = male; 0 = female)",font="arial 11").place(x=20,y=130)
     Label(Icon_window,text="cp - chest pain type (0 = typical angina; 1 = atypical angina; 2 = non-anginal pain; 3 = asymptomatic)",font="arial 11").place(x=20,y=160)
     Label(Icon_window,text="trestbps - resting blood pressure (in mm Hg on admission to the hospital)",font="arial 11").place(x=20,y=190)
     Label(Icon_window,text="chol - serum cholestoral in mg/dl",font="arial 11").place(x=20,y=220)
     Label(Icon_window,text="fbs - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)",font="arial 11").place(x=20,y=250)
     Label(Icon_window,text="restecg - resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)",font="arial 11").place(x=20,y=280)
     Label(Icon_window,text="thalach - maximum heart rate achieved",font="arial 11").place(x=20,y=310)
     Label(Icon_window,text="exang - exercise induced angina (1 = yes; 0 = no)",font="arial 11").place(x=20,y=340)
     Label(Icon_window,text="oldpeak - ST depression induced by exercise relative to rest",font="arial 11").place(x=20,y=370)
     Label(Icon_window,text="slope - the slope of the peak exercise ST segment (0 = upsloping; 1 = flat; 2 = downsloping)",font="arial 11").place(x=20,y=400)
     Label(Icon_window,text="ca - number of major vessels (0-3) colored by flourosopy",font="arial 11").place(x=20,y=430)
     Label(Icon_window,text="thal - 0 = normal; 1 = fixed defect; 2 = reversable defect",font="arial 11").place(x=20,y=460)


     Icon_window.mainloop()


### it is use for closing window
def logout():
     root.destroy()


###### clear (with the help of clear we can clear more entry filed in once )
def clear():
     Name.set('')
     DOB.set('')
     trestbps.set('')
     chol.set('')
     thalach.set('')
     oldpeak.set('')
     



########Save

def Save():
     B2=Name.get()
     C2=Date.get()
     D2=DOB.get()

     birth_date = datetime.strptime(D2, "%d/%m/%Y").date()
     today = date.today()
     E2 = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


     # today = datetime.date.today()
     # E2=today.year-DOB.get()

     try:
          F2=selection()
     except:
          messagebox.showerror("Mission Data","Please select Gender!")
     try:
          J2=selection2()
     except:
          messagebox.showerror("Mission Data","Please select fbs!")          
     try:
          M2=selection3()
     except:
          messagebox.showerror("Mission Data","Please select Exang!")
     try:
          G2=selection4()
     except:
          messagebox.showerror("Mission Data","Please select cp!")
     try:
          K2=restecg_comobobox.get()
     except:
          messagebox.showerror("Mission Data","Please select restecg!")
     try:
          O2=selection5()
     except:
          messagebox.showerror("Mission Data","Please select slope!")
     try:
          P2=ca_comobobox.get()
     except:
          messagebox.showerror("Mission Data","Please select ca!")
     try:
          Q2=thal_comobobox.get()
     except:
          messagebox.showerror("Mission Data","Please select thal!")

     H2=trestbps.get()
     I2=chol.get()
     L2=thalach.get()
     N2=float(oldpeak.get())

     print("Reg NO: %s" % B2)
     print(C2)
     print(D2)
     print(E2)
     print(F2)
     print(G2)
     print("ID: %s" % H2)
     print(I2)
     print(J2)
     print(K2)
     print(L2)
     print(M2)
     print(O2)
     print(P2)
     print(Q2)
     
     Save_Data_MySql(B2, C2, D2, int(E2), int(F2), int(G2), int(H2), int(I2), int(J2),
                         int(K2), int(L2), int(M2), float(N2), int(O2), int(P2), int(Q2),
                         int(prediction[0]))


     # Save_Data_MySql(B2,C2,D2,int(E2),int(F2),int(G2),int(H2),int(I2),int(J2),int(K2),int(L2),int(M2),float(N2),int(O2),int(P2),int(Q2),int(prediction[0]))

     # def genrate_report():
     from reportlab.pdfgen import canvas
     from reportlab.lib.pagesizes import letter
     from tkinter import messagebox, filedialog, Toplevel
     import mysql.connector

     try:
        mydb = mysql.connector.connect(host='localhost', user='root', password="roots@1210", database="heart_data")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM data ORDER BY user DESC LIMIT 1")
        info = mycursor.fetchone()

        if not info:
            messagebox.showerror("Error", "No recent patient record found.")
            

        report_window = Toplevel()
        report_window.title("Patient Report")
        report_window.geometry("600x700")

        text_area = tk.Text(report_window, wrap=tk.WORD, font=("Arial", 12))
        text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        report_content = f"""
        Heart Attack Prediction Report
        -------------------------------------
        Patient Information:
        Name: {info[1]}
        Date: {info[2]}
        Birth Date: {info[3]}
        Age: {info[4]}
        Sex: {info[5]}

        Test Results:
        Chest Pain Type: {info[6]}
        Resting Blood Pressure: {info[7]}
        Cholesterol: {info[8]}
        Fasting Blood Sugar: {info[9]}
        Resting ECG: {info[10]}
        Maximum Heart Rate: {info[11]}
        Exercise Induced Angina: {info[12]}
        Oldpeak: {info[13]}
        Slope: {info[14]}
        Calcium Score: {info[15]}
        Thalassemia: {info[16]}

        Prediction Result: {info[17]}
        """

        text_area.insert(tk.END, report_content)

        def save_to_pdf():
            file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if not file_path:
                return

            c = canvas.Canvas(file_path, pagesize=letter)
            width, height = letter
            c.setFont("Helvetica", 12)
            y = height - 40

            for line in report_content.strip().split('\n'):
                c.drawString(50, y, line.strip())
                y -= 20
                if y < 50:
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    y = height - 40

            c.save()
            messagebox.showinfo("Success", "Report saved successfully!")

        save_button = tk.Button(report_window, text="Save as PDF", command=save_to_pdf, font=("Arial", 12), bg="lightblue")
        save_button.pack(pady=10)

     except Exception as e:
        messagebox.showerror("Report Error", str(e))


     #root.destroy()
    ###### os.system("main.py")

from PIL import Image, ImageTk
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
###commentd on 14 Feb 

#icon 1
image_icon=PhotoImage(file="Image/icon.png")
#image_icon=PhotoImage(file="C:\\Users\\NIKHIL\\OneDrive\\Desktop\\project - Copy\\Image\\.png")
root.iconphoto(False,image_icon)

###end commentd on 14 Feb
'''
###added on 14 feb 2025#
image = Image.open("C:\\Users\\NIKHIL\\OneDrive\\Desktop\\project - Copy\\Image\\icon.png")
icon = ImageTk.PhotoImage(image)
icon = ImageTk.PhotoImage(image)
root.icon=icon
root.iconphoto(False, root.icon) 

'''
#header section 2
logo=PhotoImage(file="Image/header.png")
myimage=Label(image=logo,bg=background)
myimage.place(x=0,y=0)



#<<<<<<<frame 3
Heading_entry=Frame(root,width=800,height=190,bg="#df2d4b")
Heading_entry.place(x=600,y=20)

Label(Heading_entry,text="Registraion No.",font="arial 13",bg="#df2d4b",fg=framefg).place(x=30,y=0)
Label(Heading_entry,text="Date",font="arial 13",bg="#df2d4b",fg=framefg).place(x=430,y=0)

Label(Heading_entry,text="Patient Name",font="arial 13",bg="#df2d4b",fg=framefg).place(x=30,y=90)






# # Connect to MySQL
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="roots@1210",
#     database="heart_data"
# )
# cursor = conn.cursor()

# # Function to check uniqueness
# def check_and_insert():
#     patient_name = name_entry.get().strip()
    
#     if not patient_name:
#         messagebox.showwarning("Warning", "Patient Name cannot be empty!")
#         return
    
#     # Query to check if the name already exists
#     cursor.execute("SELECT COUNT(*) FROM patients WHERE name = %s", (patient_name,))
#     result = cursor.fetchone()

#     if result[0] > 0:
#         messagebox.showerror("Error", "Patient Name already exists! Please choose a different name.")
#     else:
#         # Insert new patient if unique
#         cursor.execute("INSERT INTO patients (name) VALUES (%s)", (patient_name,))
#         conn.commit()
#         messagebox.showinfo("Success", "Patient added successfully!")
# Label - using .place only (no .pack needed)
 
label = tk.Label(Heading_entry, text="Birth Date", font=("Arial", 18, "bold"),
                 bg="#df2d4b", fg=framefg)
label.place(x=430, y=90)






Entry_image=PhotoImage(file="Image/Rounded Rectangle 1.png")
Entry_image2=PhotoImage(file="Image/Rounded Rectangle 2.png")
Label(Heading_entry,image=Entry_image,bg="#df2d4b").place(x=20,y=30)
Label(Heading_entry,image=Entry_image,bg="#df2d4b").place(x=430,y=30)

Label(Heading_entry,image=Entry_image2,bg="#df2d4b").place(x=20,y=120)
Label(Heading_entry,image=Entry_image2,bg="#df2d4b").place(x=430,y=120)

Registration=IntVar()
reg_entry= Entry(Heading_entry,textvariable=Registration,width=30,font="arial 15",bg="#0e5363",fg="white",bd=0)
reg_entry.place(x=30,y=45)

Date =StringVar()
today =date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry =Entry(Heading_entry,textvariable=Date,width=15,font="arial 15",bg="#0e5363",fg="white",bd=0)
date_entry.place(x=500,y=45)
Date.set(d1)


Name=StringVar()
name_entry= Entry(Heading_entry,textvariable=Name,width=20,font="arial 20",bg="#ededed",fg="#222222",bd=0)
name_entry.place(x=30,y=130)


DOB=StringVar()
# Calendar Date Picker
birth_date = DateEntry(Heading_entry, width=21, background="darkblue",textvariable=DOB,
                       foreground="#222222", borderwidth=2, date_pattern='dd/mm/yyyy',
                       font=("Arial", 14))  # Optional: larger entry text
birth_date.place(x=450, y=130)


#dob_entry= Entry(Heading_entry,textvariable=DOB,width=20,font="arial 20",bg="#ededed",fg="#222222",bd=0)

#dob_entry.place(x=450,y=130)

#################################### Body ############################################################# 4
Detail_entry=Frame(root,width=490,height=260,bg="#dbe0e3")
Detail_entry.place(x=30,y=450)

########################radio button ############### 5
Label(Detail_entry,text="sex:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=10)
Label(Detail_entry,text="fbs:",font="arial 13",bg=framebg,fg=framefg).place(x=180,y=10)
Label(Detail_entry,text="exang:",font="arial 13",bg=framebg,fg=framefg).place(x=335,y=10)


def selection():
    if gen.get()==1:
         Gender=1
         return(Gender)
         print(Gender)
    elif gen.get()==2:
          Gender=0
          return(Gender)
          print(Gender)
    else:
         print(Gender)


def selection2():
    if fbs.get()==1:
         Fbs=1
         return(Fbs)
         print(Fbs)
    elif fbs.get()==2:
          Fbs=0
          return(Fbs)
          print(Fbs)
    else:
         print(Fbs)       
    

def selection3():
    if exang.get()==1:
         Exang=1
         return(Exang)
         print(Exang)
    elif exang.get()==2:
          Exang=0
          return(Exang)
          print(Exang)
    else:
         print(Exang)

gen= IntVar()
R1= Radiobutton(Detail_entry,text='Male',variable=gen,value=1,command=selection)
R2= Radiobutton(Detail_entry,text='Female',variable=gen,value=2,command=selection)
R1.place(x=43,y=10)
R2.place(x=93,y=10)


fbs= IntVar()
R3= Radiobutton(Detail_entry,text='True',variable=fbs,value=1,command=selection2)
R4= Radiobutton(Detail_entry,text='False',variable=fbs,value=2,command=selection2)
R3.place(x=213,y=10)
R4.place(x=263,y=10)


exang= IntVar()
R5= Radiobutton(Detail_entry,text='Yes',variable=exang,value=1,command=selection3)
R6= Radiobutton(Detail_entry,text='No',variable=exang,value=2,command=selection3)
R5.place(x=387,y=10)
R6.place(x=430,y=10)



############################## Combobox ########################### 6
Label(Detail_entry,text="cp:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=50)
Label(Detail_entry,text="restecg:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=90)
Label(Detail_entry,text="slope:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=130)
Label(Detail_entry,text="ca:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=170)
Label(Detail_entry,text="thal:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=210)

def selection4():
     input=cp_comobobox.get()
     if input=='0 = typical angina':
          return(0)
     elif input=='1 = atypical angina':
          return(1)
     elif input=='2 = non-anginal pain':
          return(2)
     elif input=='3 = asymptomatic':
          return(3)
     else :
          print(Exang)

def selection5():
     input=slope_comobobox.get()
     if input=='0 = upsloping':
          return(0)
     elif input=='1 = flat':
          return(1)
     elif input=='2 = downsloping':
          return(2)
     else :
          print(Exang)          



cp_comobobox=Combobox(Detail_entry,values=['0 = typical angina','1 = atypical angina','2 = non-anginal pain','3 = asymptomatic'],font="arial 12",state="r",width=10)
restecg_comobobox=Combobox(Detail_entry,values=['0 ','1','2'],font="arial 12",state="r",width=11)
slope_comobobox=Combobox(Detail_entry,values=['0 = upsloping','1 = flat','2 = downsloping'],font="arial 12",state="r",width=12)
ca_comobobox=Combobox(Detail_entry,values=['0','1','2','3','4'],font="arial 12",state="r",width=14)
thal_comobobox=Combobox(Detail_entry,values=['0','1','2','3','4'],font="arial 12",state="r",width=14)


cp_comobobox.place(x=50,y=50)
restecg_comobobox.place(x=80,y=90)
slope_comobobox.place(x=70,y=130)
ca_comobobox.place(x=50,y=170)
thal_comobobox.place(x=50,y=210)



####################### Entry box ########################################## 7
Label(Detail_entry,text="Smoking:",font="arial 13",width=7,bg="#dbe0e3",fg="black").place(x=240,y=50)
Label(Detail_entry,text="trestbps:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=90)
Label(Detail_entry,text="chol:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=130)
Label(Detail_entry,text="thalach:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=170)
Label(Detail_entry,text="oldpeak:",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=210)


trestbps=StringVar()
chol=StringVar()
thalach=StringVar()
oldpeak=StringVar()

trestbps_entry =Entry(Detail_entry,textvariable=trestbps,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
chol_entry =Entry(Detail_entry,textvariable=chol,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
thalach_entry =Entry(Detail_entry,textvariable=thalach,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
oldpeak_entry =Entry(Detail_entry,textvariable=oldpeak,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
trestbps_entry.place(x=320,y=90)
chol_entry.place(x=320,y=130)
thalach_entry.place(x=320,y=170)
oldpeak_entry.place(x=320,y=210)

###############################################################################################


############Report ################################################################# 8
square_report_image=PhotoImage(file="Image/Report.png")
report_background=Label(image=square_report_image,bg=background)
report_background.place(x=1120,y=340)

report=Label(root,font="arial 25 bold",bg="white",fg="#8dc63f")
report.place(x=1170,y=550)

report1=Label(root,font="arial 10 bold",bg="white")
report1.place(x=1130,y=610)


#################################################################################################



#############################Graph ################################################## 9
graph_image=PhotoImage(file="Image/graph.png")
Label(image=graph_image).place(x=600,y=270)
Label(image=graph_image).place(x=860,y=270)
Label(image=graph_image).place(x=600,y=500)
Label(image=graph_image).place(x=860,y=500)



############## Button ####################################################################### 10
analysis_button=PhotoImage(file="Image/Analysis.png")
Button(root,image=analysis_button,bd=0,bg=background,cursor='hand2',command=analysis).place(x=1130,y=240)


############# info button ##############################################
info_button=PhotoImage(file="Image/info.png")
Button(root,image=info_button,bd=0,bg=background,cursor='hand2',command=Info).place(x=10,y=240)


save_button=PhotoImage(file="Image/save.png")
Button(root,image=save_button,bd=0,bg=background,cursor='hand2',command=Save).place(x=1370,y=250)



# ##########
# import mysql.connector
# import tkinter as tk
# from tkinter import messagebox, filedialog, Toplevel, PhotoImage
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# # # ✅ Create the main Tkinter window


# # ✅ Function to Fetch the Latest Record from MySQL Database
# def  Save_Data_MySql():
#     try:
#         mydb = mysql.connector.connect(host='localhost', user='root', password="roots@1210", database="heart_data")
#         mycursor = mydb.cursor(dictionary=True)  # dictionary=True gives column names
#         mycursor.execute("SELECT * FROM data ORDER BY user DESC LIMIT 1")  # Get the latest record
#         record = mycursor.fetchone()
#         mydb.close()
#         return record
#     except mysql.connector.Error as e:
#         messagebox.showerror("Database Error", f"Failed to fetch record: {e}")
#         return None

# # ✅ Function to Generate and Display the Report
# def generate_report(info):
#     report_window = Toplevel()
#     report_window.title("Patient Report")
#     report_window.geometry("600x700")

#     text_area = tk.Text(report_window, wrap=tk.WORD, font=("Arial", 12))
#     text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

#     report_content = f"""
#     Heart Attack Prediction Report
#     -------------------------------------
#     Patient Information:
#     Name: {info.get('Name', 'N/A')}
#     Date: {info.get('Date', 'N/A')}
#     Birth Year: {info.get('DOB', 'N/A')}
#     Age: {info.get('age', 'N/A')}
#     Sex: {info.get('sex', 'N/A')}
    
#     Test Results:
#     Chest Pain Type: {info.get('Cp', 'N/A')}
#     Resting Blood Pressure: {info.get('trestbps', 'N/A')}
#     Cholesterol: {info.get('chol', 'N/A')}
#     Fasting Blood Sugar: {info.get('fbs', 'N/A')}
#     Resting ECG: {info.get('restecg', 'N/A')}
#     Maximum Heart Rate: {info.get('thalach', 'N/A')}
#     Exercise-Induced Angina: {info.get('exang', 'N/A')}
#     Oldpeak: {info.get('oldpeak', 'N/A')}
#     Slope: {info.get('slope', 'N/A')}
#     Calcium Score: {info.get('ca', 'N/A')}
#     Thalassemia: {info.get('thal', 'N/A')}
    
#     Prediction Result:
#     {info.get('result', 'N/A')}
    
#     Doctor Recommendations:
#     {'Consult a cardiologist' if info.get('result', 'N/A') == 'Positive' else 'No recommendations required.'}
# #     """

#     text_area.insert(tk.END, report_content)

#     # ✅ Function to Save Report as PDF
#     def save_to_pdf():
#         file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
#         if not file_path:
#             return
        
#         c = canvas.Canvas(file_path, pagesize=letter)
#         width, height = letter
#         c.setFont("Helvetica", 12)
#         y_position = height - 40
        
#         for line in report_content.split('\n'):
#             c.drawString(50, y_position, line)
#             y_position -= 20
#             if y_position < 50:
#                 c.showPage()
#                 c.setFont("Helvetica", 12)
#                 y_position = height - 40
        
#         c.save()
#         messagebox.showinfo("Success", "Report saved successfully!")

#     save_button = tk.Button(report_window, text="Save as PDF", command=save_to_pdf, font=("Arial", 12), bg="lightblue")
#     save_button.pack(pady=10)

# # ✅ Function Called When Save Button is Clicked
# def on_save_button_click():
#     record =  Save_Data_MySql()  # Fetch the latest patient record
#     if record:
#         generate_report(record)  # Generate report with actual database data
#     else:
#         messagebox.showerror("Error", "No record found in the database!")

# # ✅ Load the Save Button Image
# try:
#     save_button_img = PhotoImage(file="Image/save.png")  # Ensure the image path is correct
# except:
#     save_button_img = None  # If image fails to load, use text instead

# # ✅ Create the Save Button
# if save_button_img:
#     save_button = tk.Button(root, image=save_button_img, bd=0, bg="white", cursor='hand2', command=Save)
# else:
#     save_button = tk.Button(root, text="Save Report", font=("Arial", 12), bg="lightblue", command=Save)

# save_button.place(x=1370, y=700)  # Adjust position accordingly



# download_button=PhotoImage(file="Image/download.png")
# Button(root,image=download_button,bd=0,bg=background,cursor='hand2',command=on_save_button_click).place(x=1370,y=250)


'''
import tkinter as tk
from tkinter import messagebox, filedialog, Toplevel, PhotoImage
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import mysql.connector

# ✅ Connect to MySQL Database
def fetch_patient_data():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="roots@1210",  # 🔹 Replace with your MySQL password
            database="heart_data"
        )
        mycursor = mydb.cursor(dictionary=True)

        # 🔹 Fetch the latest patient record
        mycursor.execute("SELECT * FROM data ORDER BY user DESC LIMIT 1")
        patient = mycursor.fetchone()

        mydb.close()
        return patient
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error connecting to database:\n{e}")
        return None

# ✅ Function to generate and display the report
def generate_report(info, analysis, show_doctors, save):
    report_window = Toplevel()
    report_window.title("Patient Report")
    report_window.geometry("600x700")

    text_area = tk.Text(report_window, wrap=tk.WORD, font=("Arial", 12))
    text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    report_content = f"""
    Heart Attack Prediction Report
    -------------------------------------
    Patient Information:
    Name: {info.get('name', 'N/A')}
    Registration No: {info.get('reg_no', 'N/A')}
    Birth Year: {info.get('birth_year', 'N/A')}
    Date: {info.get('date', 'N/A')}
    
    Test Results:
    {save}
    
    Analysis Summary:
    {analysis}
    
    Doctor Recommendations:
    {show_doctors if show_doctors else 'No recommendations required.'}
    """

    text_area.insert(tk.END, report_content)

    # ✅ Function to save report as PDF
    def save_to_pdf():
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if not file_path:
            return
        
        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter
        c.setFont("Helvetica", 12)
        y_position = height - 40
        
        for line in report_content.split('\n'):
            c.drawString(50, y_position, line)
            y_position -= 20
            if y_position < 50:
                c.showPage()
                c.setFont("Helvetica", 12)
                y_position = height - 40
        
        c.save()
        messagebox.showinfo("Success", "Report saved successfully!")

    save_button = tk.Button(report_window, text="Save as PDF", command=save_to_pdf, font=("Arial", 12), bg="lightblue")
    save_button.pack(pady=10)

# ✅ Function called when the save button is clicked
def on_save_button_click():
    patient = fetch_patient_data()  # Fetch latest patient from database

    if patient is None:
        return  # Stop if no data is retrieved

    info = {
         "user":patient["user"],
        "Name": patient["Name"],
        "Date": patient["Date"],
        "DOB": patient["DOB"],
        "age": patient["age"],
        "sex": patient["sex"],
        "Cp":patient["Cp"],
        "trestbps":patient["trestbps"],
        "chol": patient["chol"],
        "fbs": patient["fbs"],
        "restecg": patient["restecg"],
        "thalach": patient["thalach"],
        "exang": patient["exang"],
        "oldpeak": patient["oldpeak"],
        "slope": patient["slope"],
        "ca": patient["ca"],
        "thal": patient["thal"],
        "result":patient["result"],
    }

    save = f"Cholesterol: {patient['cholesterol']} mg/dL\nBlood Pressure: {patient['blood_pressure']} mmHg"
    analysis = patient["analysis"]
    show_doctors = patient["show_doctors"]

    generate_report(info, analysis, show_doctors, save)


# Load the Save button image
try:
    save_button_img = PhotoImage(file="Image/save.png")  # Ensure correct path
except:
    save_button_img = None  # Use text if image fails to load

# ✅ Create the Save button
if save_button_img:
    save_button = tk.Button(root, image=save_button_img, bd=0, bg="white", cursor='hand2', command=on_save_button_click)
else:
    save_button = tk.Button(root, text="Save Report", font=("Arial", 12), bg="lightblue", command=on_save_button_click)

save_button.place(x=50, y=50)  # Adjust position as needed


'''



#############################################################





################################# Smoking and Non Smoking Button ##################################################### 11

button_mode=True
choice="smoking"
def changemode():
     global button_mode
     global choice

     if button_mode:
          choice="non_smoking"
          mode.config(image=non_smoking_icon,activebackground="white")
          button_mode=False
     else:
          choice="smoking"
          mode.config(image=smoking_icon,activebackground="white")
          button_mode=True

     print(choice)

smoking_icon=PhotoImage(file="Image/smoker.png")
non_smoking_icon=PhotoImage(file="Image/non-smoker.png")
mode=Button(root,image=smoking_icon,bg="#dbe0e3",bd=0,cursor="hand2",command=changemode)
mode.place(x=350,y=495)


##############################################################################################################################3

################################### LogOut Button ################################################################## 12
logout_icon=PhotoImage(file="Image/logout.png")
logout_button=Button(root,image=logout_icon,bg="#df2d4b",cursor="hand2",bd=0,command=logout)
logout_button.place(x=1390,y=60)


root.mainloop()