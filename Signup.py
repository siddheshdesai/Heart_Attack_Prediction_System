# from tkinter import *
# import tkinter as tk
# from tkinter import messagebox
# import os
# import ast

# root = tk.Tk()
# root.title("Signup")
# root.geometry("1450x730+60+80")  # Adjusted size
# root.resizable(True, True)  # Allow maximizing
# root.config(bg="#fff")

# def signup():
#     username=user.get()
#     password=code.get()
#     conform_password=conform_code.get()

#     if password==conform_password:
#         try:
#             file=open('datasheet.txt','r+')
#             d=file.read()
#             r=ast.literal_eval(d)

#             dict2={'Username':'password'}
#             r.update(dict2)
#             file.truncate(0)
#             file.close()

#             file=open('datasheet.txt','w')
#             w=file.write(str(r))
#             messagebox.showinfo('signup','Successfully sign up')

#         except:
#             file=open('datasheet.txt','w')
#             pp=str({'Username':'password'})
#             file.write(pp)
#             file.close()
#     else:
#         messagebox.showerror('Invalid',"Both Password should match")




# # Load Image
# image_icon=PhotoImage(file="Image/icon.png")
# root.iconphoto(False,image_icon)

# #header section 2
# logo=PhotoImage(file="Image/header.png")
# myimage=Label(image=logo,bg="white")
# myimage.place(x=0,y=0)


# frame=Frame(root,width=350,height=390,bg='#fff')
# frame.place(x=480,y=50)

# heading = Label(frame, text="Sign up", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
# heading.place(x=100, y=5)

# # Username Field
# def on_enter_user(e):
#     if user.get() == "Username":
#         user.delete(0, "end")

# def on_leave_user(e):
#     if user.get() == "":
#         user.insert(0, "Username")

# user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
# user.place(x=30, y=80)
# user.insert(0, "Username")
# user.bind("<FocusIn>", on_enter_user)
# user.bind("<FocusOut>", on_leave_user)
# Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

# # Password Field
# def on_enter_pass(e):
#     if code.get() == "Password":
#         code.delete(0, "end")
#         code.config(show="*")

# def on_leave_pass(e):
#     if code.get() == "":
#         code.insert(0, "Password")
#         code.config(show="")

# code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
# code.place(x=30, y=140)
# code.insert(0, "Password")
# code.bind("<FocusIn>", on_enter_pass)
# code.bind("<FocusOut>", on_leave_pass)
# Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)


# # Confirm Password Field
# def on_enter_pass2(e):
#     if conform_code.get() == "Conform Password":
#         conform_code.delete(0, "end")
#         conform_code.config(show="*")

# def on_leave_pass2(e):
#     if conform_code.get() == "":
#         conform_code.insert(0, "Conform Password")
#         conform_code.config(show="")

# conform_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
# conform_code.place(x=30, y=140)
# conform_code.insert(0, "Conform Password")
# conform_code.bind("<FocusIn>", on_enter_pass2)
# conform_code.bind("<FocusOut>", on_leave_pass2)
# Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

# # Sign-in Button
# def signin():
#     username = user.get()
#     password = code.get()

#     if username == "admin" and password == "1234":
#         screen = Toplevel(root)
#         screen.title("App")
#         screen.geometry("600x400+400+200")
#         screen.config(bg="white")
#         Label(screen, text="Hello!", bg="#fff", font=("Calibri", 50, "bold")).pack(expand=True)
#     else:
#         messagebox.showerror("Error", "Invalid username or password")

# Button(frame, width=39, pady=7, text="Sign up", bg="#57a1f8", fg="white", border=0, command=signup).place(x=35, y=204)
# # Sign-up Option
# Label(frame, text="I have an account?",fg="black",bg="white", font=("Microsoft YaHei UI Light", 9)).place(x=90, y=340)

# signin=Button(frame, width=6, text="Sign in", border=0, bg="white", cursor="hand2", fg="#57a1f8").place(x=200, y=340)






# root.mainloop()

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import ast

root = tk.Tk()
root.title("Signup")
root.geometry("1450x730+60+80")
root.resizable(True, True)
root.config(bg="#fff")

def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()  # Fixed spelling

    if password == confirm_password:
        try:
            with open('datasheet.txt', 'r+') as file:
                d = file.read()
                try:
                    r = ast.literal_eval(d)  # Convert string to dictionary
                except:
                    r = {}

                r[username] = password  # Save actual username and password
                file.seek(0)  # Move pointer to beginning
                file.truncate()  # Clear file before writing
                file.write(str(r))
            
            messagebox.showinfo('Signup', 'Successfully signed up')
        except:
            with open('datasheet.txt', 'w') as file:
                file.write(str({username: password}))  # Create new file if not exists

    else:
        messagebox.showerror('Invalid', "Both passwords should match")


def sign():
    root.destroy()

# Load Image
image_icon = PhotoImage(file="Image/icon.png")
root.iconphoto(False, image_icon)

# Header Section (Fix Placement)
logo = PhotoImage(file="Image/header.png")
myimage = Label(root, image=logo, bg="white")
myimage.place(x=0, y=0)  # Stretch across full width

# Signup Frame
frame = Frame(root, width=350, height=390, bg='#fff')
frame.place(relx=0.59, rely=0.59, anchor=CENTER)  # Dynamically center frame


heading = Label(frame, text="Sign up", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

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

# Confirm Password Field (Fixed Placement & Spelling)
def on_enter_pass2(e):
    if confirm_code.get() == "Confirm Password":
        confirm_code.delete(0, "end")
        confirm_code.config(show="*")

def on_leave_pass2(e):
    if confirm_code.get() == "":
        confirm_code.insert(0, "Confirm Password")
        confirm_code.config(show="")

confirm_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
confirm_code.place(x=30, y=200)  # Fixed overlapping issue
confirm_code.insert(0, "Confirm Password")  # Fixed spelling
confirm_code.bind("<FocusIn>", on_enter_pass2)
confirm_code.bind("<FocusOut>", on_leave_pass2)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=237)

# Sign-up Button
Button(frame, width=39, pady=7, text="Sign up", bg="#57a1f8", fg="white", border=0, command=signup).place(x=35, y=270)

# Sign-in Option
Label(frame, text="I have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9)).place(x=90, y=340)
signin=Button(frame, width=6, text="Sign in", border=0, bg="white", cursor="hand2", fg="#57a1f8",command=sign).place(x=200, y=340)


root.mainloop()
