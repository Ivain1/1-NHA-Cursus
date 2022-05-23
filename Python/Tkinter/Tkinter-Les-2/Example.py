from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("ik leer Python gui maken bij NHA")
root.geometry("640x480")

def show_message():
    messagebox.showinfo(berichtje.get(),berichtje.get())

frame = Frame(root)
frame.pack()

berichtje = StringVar()
lbl_bericht = Label(frame, width = 30, text = 'Type je berichtje')
lbl_bericht.pack()
txt_berichtje = Entry(frame, width = 30, textvariable = berichtje)
txt_berichtje.pack()
btn_show_berichtje = Button(frame,width = 25, text = 'laat berichtje zien', command = show_message)

btn_show_berichtje.pack()
root.mainloop()