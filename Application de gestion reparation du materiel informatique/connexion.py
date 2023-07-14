from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
import mysql.connector
import tkinter as tk
# from PIL import Image, ImageTk

root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)


def signin():
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '1234':
        # si le username == 'admin' and password == '1234' alors ouvre redirige nous sur la page1
        root.destroy()
        import client

        # screen.mainloop()

    elif username != 'admin' and password != '1234':
        messagebox.showerror("invalid", "mot de pass et utilisateur invalide")
    elif password != '1234':
        messagebox.showerror("invalid", "mot de pass invalide")
    elif username != 'admin':
        messagebox.showerror("invalid", "utilisateur invalide")


# img = PhotoImage(file='login.png')
# Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='sing in', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=1000, y=5)


# --------------------


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=25, fg='black', border=2,
             bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


# --------------------


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


code = Entry(frame, width=25, fg='black', border=2,
             bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

##################################

Button(frame, width=39, pady=7, text='Connexion', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)

root.mainloop()
