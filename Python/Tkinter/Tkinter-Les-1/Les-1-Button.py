from tkinter import *
from tkinter.ttk import *
WIDTH = str(300)
HEIGHT = str(250)
windowSize = WIDTH + 'x' + HEIGHT

root = Tk()
root.title("Calculator")
root.geometry(windowSize)
#calcFrame = Frame(root)
#label_frame = LabelFrame(root, text = 'Basic Calculator')
#label_frame.grid(column = 0, row = 0, padx = 10, pady = 10)

style = Style()
style.configure('TButton', font = ('verdana', 20, 'bold'),foreground = 'gray', background = 'dark gray', width = 3)

label_frame = LabelFrame(root)
label_frame.grid(column = 0, row = 0, padx = 10, pady = 10)

style.map('TButton', foreground = [('active', '!disabled', 'green')], background = [('active','black')])



txt = Entry(label_frame, width = 43, text = '0', style = 'TButton')
txt.grid(column = 1, row = 0, columnspan = 10)

button1 = Button(label_frame, text=' 1 ', style = 'TButton', command = None)
button1.grid(column = 1, row = 3)
button2 = Button(label_frame, text=' 2 ')
button2.grid(column = 2, row = 3)
button3 = Button(label_frame, text=' 3 ')
button3.grid(column = 3, row = 3)
button4 = Button(label_frame, text=' 4 ')
button4.grid(column = 1, row = 2)
button5 = Button(label_frame, text=' 5 ')
button5.grid(column = 2, row = 2)
button6 = Button(label_frame, text=' 6 ')
button6.grid(column = 3, row = 2)
button7 = Button(label_frame, text=' 7 ')
button7.grid(column = 1, row = 1)
button8 = Button(label_frame, text=' 8 ')
button8.grid(column = 2, row = 1)
button9 = Button(label_frame, text=' 9 ')
button9.grid(column = 3, row = 1)
button0 = Button(label_frame, text=' 0 ')
button0.grid(column = 2, row = 4)
buttonAdd = Button(label_frame,text=' + ')
buttonAdd.grid(column = 4, row = 4)
buttonSub = Button(label_frame,text=' - ')
buttonSub.grid(column = 4, row = 3)
buttonMul = Button(label_frame,text=' x ')
buttonMul.grid(column = 4, row = 2)
buttonDiv = Button(label_frame,text=' / ')
buttonDiv.grid(column = 4, row = 1)
buttonCalc = Button(label_frame,text=' = ')
buttonCalc.grid(column = 3, row = 4)


root.mainloop()
