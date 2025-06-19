# from tkinter import *
# from PIL import Image, ImageTk

# # Create the main window
# root = Tk()
# root.title("Heart Attack Prediction System")
# root.geometry("1450x730+60+80")
# root.resizable(True, True)

# # Set background color
# background_color = "#f0ddd5"
# root.config(bg=background_color)

# # Header Section
# header_frame = Frame(root, bg="#df2d4b", width=1450, height=100)
# header_frame.pack(side=TOP, fill=X)

# # Logo
# logo_image = PhotoImage(file="Image/header.png")  # Replace with your logo path
# logo_label = Label(header_frame, image=logo_image, bg="#df2d4b")
# logo_label.pack(side=LEFT, padx=20)

# # Title
# title_label = Label(header_frame, text="Heart Attack Prediction System", font=("Arial", 24, "bold"), bg="#df2d4b", fg="white")
# title_label.pack(side=LEFT, padx=20)

# # Welcome Message
# welcome_label = Label(root, text="Welcome to the Heart Attack Prediction System", font=("Arial", 18), bg=background_color, fg="#333")
# welcome_label.pack(pady=20)

# # Navigation Buttons
# button_frame = Frame(root, bg=background_color)
# button_frame.pack(pady=20)

# # Start Analysis Button
# start_analysis_button = Button(button_frame, text="Start Analysis", font=("Arial", 16), bg="#62a7ff", fg="white", width=20, command=lambda: print("Start Analysis"))
# start_analysis_button.grid(row=0, column=0, padx=20, pady=10)

# # View Doctors Button
# view_doctors_button = Button(button_frame, text="View Recommended Doctors", font=("Arial", 16), bg="#62a7ff", fg="white", width=20, command=lambda: print("View Doctors"))
# view_doctors_button.grid(row=0, column=1, padx=20, pady=10)

# # Info Button
# info_button = Button(button_frame, text="Info", font=("Arial", 16), bg="#62a7ff", fg="white", width=20, command=lambda: print("Info"))
# info_button.grid(row=1, column=0, padx=20, pady=10)

# # Logout Button
# logout_button = Button(button_frame, text="Logout", font=("Arial", 16), bg="#ed1c24", fg="white", width=20, command=root.quit)
# logout_button.grid(row=1, column=1, padx=20, pady=10)

# # Footer Section
# footer_frame = Frame(root, bg="#df2d4b", width=1450, height=50)
# footer_frame.pack(side=BOTTOM, fill=X)

# footer_label = Label(footer_frame, text="© 2023 Heart Attack Prediction System. All rights reserved.", font=("Arial", 10), bg="#df2d4b", fg="white")
# footer_label.pack(pady=10)

# # Run the application
# root.mainloop()

# from tkinter import *
# import webbrowser  # For opening email & website links
# from PIL import Image, ImageTk

# # Create the main window
# root = Tk()
# root.title("Heart Attack Prediction System")
# root.geometry("1450x730+60+80")
# root.resizable(True, True)

# # Set background color
# background_color = "#f0ddd5"
# root.config(bg=background_color)

# # Header Section
# header_frame = Frame(root, bg="#df2d4b", width=1450, height=100)
# header_frame.pack(side=TOP, fill=X)

# # Load and Resize Header Image
# try:
#     logo_image = Image.open("Image/header.png")  # Ensure correct path
#     logo_image = logo_image.resize((120, 80))  # Resize to fit
#     logo_photo = ImageTk.PhotoImage(logo_image)
# except Exception as e:
#     print("Error loading header image:", e)
#     logo_photo = None  # Prevent crashes if image is missing

# # Logo Label (Top-Left)
# if logo_photo:
#     logo_label = Label(header_frame, image=logo_photo, bg="#df2d4b")
#     logo_label.place(x=20, y=10)  # Adjust positioning

# # Title (Centered)
# title_label = Label(header_frame, text="Heart Attack Prediction System", font=("Arial", 24, "bold"), bg="#df2d4b", fg="white")
# title_label.place(x=500, y=30)

# # Function to Show "About Us" Information
# def about_us():
#     about_window = Toplevel(root)
#     about_window.title("About Us")
#     about_window.geometry("500x400")
#     about_window.config(bg="white")

#     Label(about_window, text="About Our System", font=("Arial", 18, "bold"), bg="white", fg="#df2d4b").pack(pady=10)
    
#     info_text = (
#         "Heart Attack Prediction System is an AI-based tool\n"
#         "that helps predict the risk of heart attacks using\n"
#         "health metrics and machine learning algorithms.\n\n"
#         "Features:\n"
#         "- Predicts heart attack risk\n"
#         "- Visual representation of health data\n"
#         "- Recommends cardiologists\n"
#         "- Secure authentication with MySQL"
#     )
    
#     Label(about_window, text=info_text, font=("Arial", 12), bg="white", justify=LEFT).pack(padx=20, pady=10)

#     Button(about_window, text="Close", font=("Arial", 12), bg="#df2d4b", fg="white", command=about_window.destroy).pack(pady=10)

# # Function to Show "Contact Us" with Hyperlinks & Feedback Form
# def contact_us():
#     contact_window = Toplevel(root)
#     contact_window.title("Contact Us")
#     contact_window.geometry("500x450")
#     contact_window.config(bg="white")

#     Label(contact_window, text="Contact Information", font=("Arial", 18, "bold"), bg="white", fg="#df2d4b").pack(pady=10)

#     # Function to open links
#     def open_email():
#         webbrowser.open("mailto:support@heartprediction.com")

#     def open_website():
#         webbrowser.open("http://www.heartprediction.com")

#     # Contact Details with Clickable Links
#     email_label = Label(contact_window, text="📧 Email: support@heartprediction.com", font=("Arial", 12), fg="blue", bg="white", cursor="hand2")
#     email_label.pack(pady=5)
#     email_label.bind("<Button-1>", lambda e: open_email())

#     website_label = Label(contact_window, text="🌐 Website: www.heartprediction.com", font=("Arial", 12), fg="blue", bg="white", cursor="hand2")
#     website_label.pack(pady=5)
#     website_label.bind("<Button-1>", lambda e: open_website())

#     Label(contact_window, text="📞 Phone: +123-456-7890", font=("Arial", 12), bg="white").pack(pady=5)

#     # Feedback Section (Centered & Larger)
#     Label(contact_window, text="💬 Leave Your Feedback:", font=("Arial", 14, "bold"), bg="white", fg="#df2d4b").pack(pady=10)

#     feedback_frame = Frame(contact_window, bg="white")  # Frame for centering
#     feedback_frame.pack(pady=5)

#     feedback_entry = Text(feedback_frame, height=5, width=55)  # Increased height
#     feedback_entry.pack(pady=5)

#     # Function to handle feedback submission
#     def submit_feedback():
#         feedback = feedback_entry.get("1.0", "end-1c")
#         if feedback.strip():
#             print("Feedback submitted:", feedback)
#             feedback_entry.delete("1.0", END)
#             Label(contact_window, text="✅ Thank you for your feedback!", fg="green", bg="white").pack(pady=5)

#     submit_button = Button(contact_window, text="Submit", font=("Arial", 12), bg="#28a745", fg="white", command=submit_feedback)
#     submit_button.pack(pady=10)

#     Button(contact_window, text="Close", font=("Arial", 12), bg="#df2d4b", fg="white", command=contact_window.destroy).pack(pady=5)

# # Top Navigation Buttons (About Us & Contact Us)
# about_button = Button(header_frame, text="About Us", font=("Arial", 14), bg="white", fg="black", width=12, command=about_us)
# about_button.place(x=1100, y=30)

# contact_button = Button(header_frame, text="Contact Us", font=("Arial", 14), bg="white", fg="black", width=12, command=contact_us)
# contact_button.place(x=1250, y=30)

# # Welcome Message (Centered)
# welcome_label = Label(root, text="Welcome to the Heart Attack Prediction System", font=("Arial", 18), bg=background_color, fg="#333")
# welcome_label.pack(pady=40)

# # Frame for Centered Content
# center_frame = Frame(root, bg=background_color)
# center_frame.pack(expand=True)

# # Start Analysis Button
# start_analysis_button = Button(center_frame, text="Start Analysis", font=("Arial", 16), bg="#62a7ff", fg="white", width=20, command=lambda: print("Start Analysis"))
# start_analysis_button.pack(pady=15)

# # Login Button
# def login_clicked():
#     print("Login Clicked")  # Replace with actual login functionality

# login_button = Button(center_frame, text="Login", font=("Arial", 16), bg="#28a745", fg="white", width=20, command=login_clicked)
# login_button.pack(pady=15)

# # Footer Section
# footer_frame = Frame(root, bg="#df2d4b", width=1450, height=50)
# footer_frame.pack(side=BOTTOM, fill=X)

# footer_label = Label(footer_frame, text="© 2025 Heart Attack Prediction System. All rights reserved.", font=("Arial", 10), bg="#df2d4b", fg="white")
# footer_label.pack(pady=10)

# # Run the application
# root.mainloop()


from tkinter import *
import webbrowser  # For opening email & website links
from PIL import Image, ImageTk


# Create the main window
root = Tk()
root.title("Heart Attack Prediction System")
root.geometry("1450x730+60+80")
root.resizable(True, True)

# Set background color
background_color = "white"
root.config(bg=background_color)

# Header Section
header_frame = Frame(root, bg="#df2d4b", width=1450, height=100)
header_frame.pack(side=TOP, fill=X)

# Load and Resize Header Image
try:
    logo_image = Image.open("Image/heartt.png")  # Ensure correct path
    logo_image = logo_image.resize((110, 80))  # Resize to fit
    logo_photo = ImageTk.PhotoImage(logo_image)
except Exception as e:
    print("Error loading header image:", e)
    logo_photo = None  # Prevent crashes if image is missing

# Logo Label (Top-Left)
if logo_photo:
    logo_label = Label(header_frame, image=logo_photo, bg="#df2d4b")
    logo_label.place(x=20, y=10)  # Adjust positioning

# Title (Centered)
title_label = Label(header_frame, text="Heart Attack Prediction System", font=("Arial", 24, "bold"), bg="#df2d4b", fg="white")
title_label.place(x=500, y=30)


#icon 1
image_icon=PhotoImage(file="Image/icon.png")
root.iconphoto(False,image_icon)

# Load and add first overlay image (Logo)
overlay1_image = Image.open("Image/drr.png")  # First overlay image
overlay1_image = overlay1_image.resize((400, 400), Image.LANCZOS)  # Resize overlay
overlay1_photo = ImageTk.PhotoImage(overlay1_image)

# Display first overlay image
overlay1_label = Label(root, image=overlay1_photo, bg="white")  # Transparent effect
overlay1_label.place(x=15, y=160)  # Adjust position


# Function to Show "About Us" Information
def about_us():
    about_window = Toplevel(root)
    about_window.title("About Us")
    about_window.geometry("500x400")
    about_window.config(bg="white")

    Label(about_window, text="About Our System", font=("Arial", 18, "bold"), bg="white", fg="#df2d4b").pack(pady=10)
    
    info_text = (
        "Heart Attack Prediction System is an AI-based tool\n"
        "that helps predict the risk of heart attacks using\n"
        "health metrics and machine learning algorithms.\n\n"
        "Features:\n"
        "- Predicts heart attack risk\n"
        "- Visual representation of health data\n"
        "- Recommends cardiologists\n"
        "- Secure authentication with MySQL"
    )
    
    Label(about_window, text=info_text, font=("Arial", 12), bg="white", justify=LEFT).pack(padx=20, pady=10)

    Button(about_window, text="Close", font=("Arial", 12), bg="#df2d4b", fg="white", command=about_window.destroy).pack(pady=10)

# Function to Show "Contact Us" with Hyperlinks & Feedback Form
def contact_us():
    contact_window = Toplevel(root)
    contact_window.title("Contact Us")
    contact_window.geometry("500x450")
    contact_window.config(bg="white")

    Label(contact_window, text="Contact Information", font=("Arial", 18, "bold"), bg="white", fg="#df2d4b").pack(pady=10)

    # Function to open links
    def open_email():
        webbrowser.open("mailto:support@heartprediction.com")

    def open_website():
        webbrowser.open("http://www.heartprediction.com")

    # Contact Details with Clickable Links
    email_label = Label(contact_window, text="📧 Email: support@heartprediction.com", font=("Arial", 12), fg="blue", bg="white", cursor="hand2")
    email_label.pack(pady=5)
    email_label.bind("<Button-1>", lambda e: open_email())

    website_label = Label(contact_window, text="🌐 Website: www.heartprediction.com", font=("Arial", 12), fg="blue", bg="white", cursor="hand2")
    website_label.pack(pady=5)
    website_label.bind("<Button-1>", lambda e: open_website())

    Label(contact_window, text="📞 Phone: +123-456-7890", font=("Arial", 12), bg="white").pack(pady=5)

    # Feedback Section (Centered & Larger)
    Label(contact_window, text="💬 Leave Your Feedback:", font=("Arial", 14, "bold"), bg="white", fg="#df2d4b").pack(pady=10)

    feedback_frame = Frame(contact_window, bg="white")  # Frame for centering
    feedback_frame.pack(pady=5)

    feedback_entry = Text(feedback_frame, height=5, width=55)  # Increased height
    feedback_entry.pack(pady=5)

    # Function to handle feedback submission
    def submit_feedback():
        feedback = feedback_entry.get("1.0", "end-1c")
        if feedback.strip():
            print("Feedback submitted:", feedback)
            feedback_entry.delete("1.0", END)
            Label(contact_window, text="✅ Thank you for your feedback!", fg="green", bg="white").pack(pady=5)

    submit_button = Button(contact_window, text="Submit", font=("Arial", 12), bg="#28a745", fg="white", command=submit_feedback)
    submit_button.pack(pady=10)

    Button(contact_window, text="Close", font=("Arial", 12), bg="#df2d4b", fg="white", command=contact_window.destroy).pack(pady=5)

# Top Navigation Buttons (About Us & Contact Us)
about_button = Button(header_frame, text="About Us", font=("Arial", 14), bg="white", fg="black", width=12, command=about_us)
about_button.place(x=1100, y=30)

contact_button = Button(header_frame, text="Contact Us", font=("Arial", 14), bg="white", fg="black", width=12, command=contact_us)
contact_button.place(x=1250, y=30)

# Welcome Message (Centered)
welcome_label = Label(root, text="Welcome to the Heart Attack Prediction System", font=("Arial", 18), bg=background_color, fg="#333")
welcome_label.pack(pady=40)

# Frame for Centered Content
center_frame = Frame(root, bg=background_color)
center_frame.pack(expand=True)

# Login Button
import subprocess  # Import subprocess to run another script
import tkinter as tk

# Login Button Function
def login_clicked():
    #import Login
    #print("Hiii")
    subprocess.run(["python", "login.py"])  # Runs login.py
    
# Create Login Button
login_button = Button(center_frame, text="Login", font=("Arial", 16), bg="#28a745", fg="white", width=20,command=login_clicked)
login_button.pack(pady=15)

# Function to show heart health precautions
def show_precautions():
    precautions_window = Toplevel(root)
    precautions_window.title("Heart Health Precautions")
    precautions_window.geometry("500x400")
    precautions_window.config(bg="white")

    Label(precautions_window, text="Heart Health Precautions", font=("Arial", 18, "bold"), bg="white", fg="#df2d4b").pack(pady=10)
    
    precautions_text = (
        "✅ Eat a healthy diet (fruits, vegetables, whole grains).\n"
        "✅ Exercise regularly (at least 30 mins per day).\n"
        "✅ Avoid smoking and limit alcohol intake.\n"
        "✅ Maintain a healthy weight.\n"
        "✅ Manage stress with relaxation techniques.\n"
        "✅ Monitor your blood pressure and cholesterol levels.\n"
        "✅ Get regular heart check-ups.\n"
        "✅ Stay hydrated and get enough sleep.\n"
    )
    
    Label(precautions_window, text=precautions_text, font=("Arial", 12), bg="white", justify=LEFT).pack(padx=20, pady=10)

    Button(precautions_window, text="Close", font=("Arial", 12), bg="#df2d4b", fg="white", command=precautions_window.destroy).pack(pady=10)

# Footer Section
footer_frame = Frame(root, bg="#df2d4b", width=1450, height=60)
footer_frame.pack(side=BOTTOM, fill=X)

# Precautions Button (Bottom of Home Page)
precautions_button = Button(footer_frame, text="Heart Health Precautions", font=("Arial", 12), bg="white", fg="black", command=show_precautions)
precautions_button.pack(pady=10)

footer_label = Label(footer_frame, text="© 2025 Heart Attack Prediction System. All rights reserved.", font=("Arial", 10), bg="#df2d4b", fg="white")
footer_label.pack(pady=10)

# Run the application
root.mainloop()
#root.destroy()











