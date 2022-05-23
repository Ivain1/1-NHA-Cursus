from tkinter import *


root = Tk()

root.geometry("500x500")

name_var = StringVar()
passw_var = StringVar()

def submit():
    name = name_var.get()
    password = passw_var.get()

    print("the name is" + name)
    print("the password is" + password)

    name_var.set("")
    passw_var.set("")


name_label = Label(root, text='Username', font=('calibre', 10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))

# creating a label for password
passw_label = Label(root, text='Password', font=('calibre', 10, 'bold'))

# creating a entry for password
passw_entry = Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')

# creating a button using the widget
# Button that will call the submit function
sub_btn = Button(root, text='Submit', command=submit)

# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

root.mainloop()