from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import os
import subprocess

root = tk.Tk()
root.title("Login")
root.geometry("1450x730+60+80")
root.resizable(True, True)
root.config(bg="#fff")

# Database Connection Function
def connect_db():
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password="roots@1210",
            database="heart_data"
        )
        return mydb
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database connection failed: {err}")
        return None

# Sign-in Function
def signin():
    username = user.get()
    password = code.get()

    if username == '' or password == '':
        messagebox.showerror("Error", "Please fill in all fields")
        return

    mydb = connect_db()
    if mydb:
        mycursor = mydb.cursor()
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        mycursor.execute(query, (username, password))
        row = mycursor.fetchone()

        if row is None:
            messagebox.showerror("Error", "Invalid username or password")
        else:
            #messagebox.showinfo("Success", "Login successful")
            #os.system("main.py")
            print("Hiiiiii")
            subprocess.run(["python", "Main.py"])
            #import Main
            #root.destroy()  # Close login window after success
            #os.system("main.py")

        mycursor.close()
        mydb.close()

# Signup Window
def connect_database():
    window = Toplevel(root)
    window.geometry("1450x730+60+80")
    window.resizable(True, True)
    window.config(bg="#fff")

    # Keep a reference to prevent garbage collection
    window.logo = PhotoImage(file="Image/header.png")  
    myimage = Label(window, image=window.logo, bg="white")
    myimage.place(x=0, y=0)  # Place the image properly

    # Load and set window icon
    window.image_icon = PhotoImage(file="Image/icon.png")
    window.iconphoto(False, window.image_icon)

    # Sign-up frame
    frame = Frame(window, width=350, height=390, bg='#fff')
    frame.place(relx=0.59, rely=0.59, anchor=CENTER)

    Label(frame, text="Sign up", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold")).place(x=100, y=5)








    def signup():
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()

        if username == '' or password == '' or confirm_password == '':
            messagebox.showerror("Error", "Please fill all fields")
            return
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        mydb = connect_db()
        if mydb:
            mycursor = mydb.cursor()

            # Check if user already exists
            mycursor.execute("SELECT * FROM users WHERE username=%s", (username,))
            existing_user = mycursor.fetchone()

            if existing_user:
                messagebox.showerror("Error", "Username already exists. Choose another.")
            else:
                insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                mycursor.execute(insert_query, (username, password))
                mydb.commit()
                messagebox.showinfo("Success", "Signup successful!")
                window.destroy()  # Close signup window after success

            mycursor.close()
            mydb.close()
            

    def sign():
        window.destroy()

 

   # Label(frame, text="Sign up", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold")).place(x=100, y=5)
    

    def on_enter_user(e):
        if user.get() == "Username":
            user.delete(0, "end")

    def on_leave_user(e):
        if user.get() == "":
            user.insert(0, "Username")

    user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", on_enter_user)
    user.bind("<FocusOut>", on_leave_user)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

    def on_enter_pass(e):
        if code.get() == "Password":
            code.delete(0, "end")
            code.config(show="*")

    def on_leave_pass(e):
        if code.get() == "":
            code.insert(0, "Password")
            code.config(show="")

    code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    code.place(x=30, y=140)
    code.insert(0, "Password")
    code.bind("<FocusIn>", on_enter_pass)
    code.bind("<FocusOut>", on_leave_pass)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

    def on_enter_pass2(e):
        if confirm_code.get() == "Confirm Password":
            confirm_code.delete(0, "end")
            confirm_code.config(show="*")

    def on_leave_pass2(e):
        if confirm_code.get() == "":
            confirm_code.insert(0, "Confirm Password")
            confirm_code.config(show="")

    confirm_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
    confirm_code.place(x=30, y=200)
    confirm_code.insert(0, "Confirm Password")
    confirm_code.bind("<FocusIn>", on_enter_pass2)
    confirm_code.bind("<FocusOut>", on_leave_pass2)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=237)

    Button(frame, width=39, pady=7, text="Sign up", bg="#57a1f8", fg="white", border=0, command=signup).place(x=35, y=270)
    Label(frame, text="I have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9)).place(x=90, y=340)
    Button(frame, width=6, text="Sign in", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=sign).place(x=200, y=340)

    

 # Load Image
image_icon=PhotoImage(file="Image/icon.png")
root.iconphoto(False,image_icon)

 #header section 2
logo=PhotoImage(file="Image/header.png")
myimage=Label(image=logo,bg="white")
myimage.place(x=0,y=0)

# Login UI
frame = Frame(root, width=350, height=350, bg="white")
frame.place(relx=0.59, rely=0.59, anchor=CENTER) # Dynamically center frame

Label(frame, text="Log in", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold")).place(x=100, y=5)

# Username Field
def on_enter_user(e):
    if user.get() == "Username":
        user.delete(0, "end")

def on_leave_user(e):
    if user.get() == "":
        user.insert(0, "Username")

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter_user)
user.bind("<FocusOut>", on_leave_user)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

# Password Field
def on_enter_pass(e):
    if code.get() == "Password":
        code.delete(0, "end")
        code.config(show="*")

def on_leave_pass(e):
    if code.get() == "":
        code.insert(0, "Password")
        code.config(show="")

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=140)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enter_pass)
code.bind("<FocusOut>", on_leave_pass)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

Button(frame, width=39, pady=7, text="Sign in", bg="#57a1f8", fg="white", border=0, command=signin).place(x=35, y=204)
Label(frame, text="Don't have an account?", fg="black", bg="white").place(x=75, y=270)
Button(frame, width=6, text="Sign up", border=0, bg="white", fg="#57a1f8", command=connect_database).place(x=215, y=270)

root.mainloop()