from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
WIDTH = str(300)
HEIGHT = str(250)
windowSize = WIDTH + 'x' + HEIGHT
typeNum = ""
displayNum = ""
storeNum1 = []
storeNum2 = []

root = Tk()
root.title("Calculator")
root.geometry(windowSize)
#calcFrame = Frame(root)
#frame = LabelFrame(root, text = 'Basic Calculator')
#frame.grid(column = 0, row = 0, padx = 10, pady = 10)

style = Style()
style.configure('TButton', font = ('verdana', 20, 'bold'),foreground = 'black', background = 'dark gray', width = 3)

#labelStyle = Style()
#labelStyle.configure('CLabel', font =('verdana', 16), foreground = 'black', background = 'dark gray', width = 3)

frame = Frame(root)
frame.pack()

style.map('TButton', foreground = [('active', '!disabled', 'green')], background = [('active','black')])
#labelStyle.map('CLabel', foreground = [('active', '!disabled', 'green')], background = [('active','black')])

#lbl = Label(frame, text= typeNum, style = 'TButton')
#lbl.grid(column = 1, row = 5)
txt = Label(frame, text = typeNum, width = 10)
txt.grid(column=1, row=0)

def displayNumber():
    #for i in len(typeNum):
     #   displayNum = displayNum + str(typeNum[i])
    #print(displayNum)
    txt = Label(frame, text = typeNum, width = 10)
    txt.grid(column=1, row=0)

def addNumber(num1):
    displayNum = typeNum + str(num1)
    print(displayNum)





#def calculate():


totalMessage = typeNum
print(totalMessage)
#txt = Entry(frame, width = 43, style = 'TButton', textvariable = totalMessage)
#txt.grid(column = 1, row = 0, columnspan = 10)



button1 = Button(frame, text=' 1 ', command = lambda: addNumber(1))
button1.grid(column = 1, row = 3)
button2 = Button(frame, text=' 2 ', command = lambda: addNumber(2))
button2.grid(column = 2, row = 3)
button3 = Button(frame, text=' 3 ', command = lambda: addNumber(3))
button3.grid(column = 3, row = 3)
button4 = Button(frame, text=' 4 ', command = lambda: addNumber(4))
button4.grid(column = 1, row = 2)
button5 = Button(frame, text=' 5 ', command = lambda: addNumber(5))
button5.grid(column = 2, row = 2)
button6 = Button(frame, text=' 6 ', command = lambda: addNumber(6))
button6.grid(column = 3, row = 2)
button7 = Button(frame, text=' 7 ', command = lambda: addNumber(7))
button7.grid(column = 1, row = 1)
button8 = Button(frame, text=' 8 ', command = lambda: addNumber(8))
button8.grid(column = 2, row = 1)
button9 = Button(frame, text=' 9 ', command = lambda: addNumber(9))
button9.grid(column = 3, row = 1)
button0 = Button(frame, text=' 0 ', command = lambda: addNumber(0))
button0.grid(column = 2, row = 4)
buttonAdd = Button(frame,text=' + ')
buttonAdd.grid(column = 4, row = 4)
buttonSub = Button(frame,text=' - ')
buttonSub.grid(column = 4, row = 3)
buttonMul = Button(frame,text=' x ')
buttonMul.grid(column = 4, row = 2)
buttonDiv = Button(frame,text=' / ')
buttonDiv.grid(column = 4, row = 1)
buttonCalc = Button(frame,text=' = ')
buttonCalc.grid(column = 3, row = 4)


root.mainloop()
