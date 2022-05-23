from tkinter import *
import tkinter as tk
from tkinter.ttk import Style

screen_width = 1000
screen_height = 480
screen_size = str(screen_width) + 'x' + str(screen_height)
master = Tk()

master.title('General Hospital Login')
master.minsize(600,400)
master.maxsize(800,500)
master.geometry(screen_size)
master.configure(background = 'light blue')

#centerFrame = Frame(master, width = 400, height = 200, bg = 'light grey')

registerFrame = Frame(master, width = 400, height = 180, bg = 'light grey')
registerFrame.grid(column = 0, row = 0, padx = (screen_width/4.5), pady = (screen_height/4.8))
#registerFrame.configure(background = 'gray')
global email1
global email2
#style.configure('hStyle', background = 'dark gray', foreground = 'white', font = ('Verdana', 16))
mail_1 = StringVar()
mail_2 = StringVar()
Pass = StringVar()

def register():
    mail_1 = 'mail1'
    mail_2 = 'mail2'
    email1 = mail_1.get()
    email2 = mail_2.get()
    if mail_1 == mail_2:
        print('mails match')
    else:
        print('Email error')

titleLabel = Label(registerFrame, text = 'Welcome to the General Hospital', font =('Verdana', 16), fg = 'dark blue', bg = 'light Blue')

subLabel = Label(registerFrame, text = 'Please log in here:', font=('Verdana',12), fg = 'dark blue', bg = 'light gray')

label1 = Label(registerFrame, text = "Email: ", font=('Verdana', 10), fg = 'dark blue', bg = 'light gray')
label2 = Label(registerFrame, text = "Confirm Email: ", font=('Verdana', 10), fg = 'dark blue', bg = 'light gray')
emailMain = Entry(registerFrame, textvariable = mail_1)
emailCheck = Entry(registerFrame, textvariable = mail_2)
passwordIn = Entry(registerFrame, textvariable = Pass, show='*')
passLabel = Label(registerFrame, text = 'Password', font=('Verdana',10), fg = 'dark blue', bg = 'light gray')
titleLabel.grid(column = 0, row = 0, columnspan = 3, sticky = W, pady = 2)
subLabel.grid(column = 0, row = 1, columnspan=4, sticky= W)
label1.grid(column = 0, row = 2, sticky = W)
label2.grid(column = 0, row = 3, sticky = W)
passLabel.grid(column = 0, row = 4, sticky = W)
emailMain.grid(column = 1, row = 2, sticky = E)
emailCheck.grid(column = 1, row = 3, sticky = E)
passwordIn.grid(column = 1, row = 4, sticky = E)



registerButton = Button(registerFrame, text = 'Register', command = register)
registerButton.grid(column = 1, row = 5, sticky = S, padx = 10)

def openNewWindow():
    newWindow = Toplevel(master)
    newWindow.title('New Window')
    newWindow.geometry(screen_size)
    Label(newWindow, text = "This is a new window")




master.mainloop()