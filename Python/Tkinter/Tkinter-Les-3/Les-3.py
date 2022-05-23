from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Style
windowWidth = 400
windowHeight = 200
windowSize = str(windowWidth) + 'x' + str(windowHeight)
global internal_dict = dict()


def callback():
    emailIn = str(email.get())
    checking = messagebox.askyesno("email-check", "Is this the correct email?\n" + emailIn)
    #print(checking)
    return(checking)

def saveInfo(data1,data2):
    internal_dict = {}

    internal_dict[str(data1)] = str(data2)
    print(str(internal_dict))
#def compare():



root = Tk()

root.title("Login Screen")

root.geometry(windowSize)

frame = Frame()
frame.pack(side = TOP, anchor = CENTER, fill = Y)
style = Style()
style.configure()

email = StringVar()
email2 = StringVar()
password = StringVar()
loginMessage = "To log in, you need to register yourself first. \n Please do so here:"
intro = Label(frame, text = loginMessage).grid(column = 0, row = 0, columnspan = 2)
l = Label(frame, text = "Email : ").grid(column = 0, row = 1, sticky = E)
e = Entry(frame, bd=1, textvariable = email, validate = "focusout", validatecommand = callback).grid(column = 1, row = 1, sticky = E)
ec = Entry(frame, bd=1, textvariable = email2, validate = "focusout", validatecommand = callback).grid(column = 1, row = 2, sticky = E)
confirm_label = Label(frame, text = "Confirm Email :").grid(column = 0, row =2, sticky = E)
p_label = Label(frame, text = 'Password :').grid(column = 0, row = 3, sticky = E)
p_entry = Entry(frame, show = "*", textvariable = password).grid(column = 1, row = 3, sticky = E)
b_confirm = Button(frame,text = 'Confirm', command = lambda: saveInfo(email, password)).grid(column = 1, row = 4, sticky = S, columnspan = 1)
storage = Label(frame, textvariable = internal_dict).grid(column = 1, row = 5, sticky = S, columnspan = 1)




root.mainloop()