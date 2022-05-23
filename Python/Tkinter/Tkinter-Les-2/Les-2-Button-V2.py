import tkinter
from tkinter import *
#from tkinter import font
#from tkinter.ttk import Style
#from tkinter.ttk import Button
expression = ""



def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)

def calculate():
    try:
        global expression

        total = str(eval(expression))

        equation.set(total)


        expression = ""

    except:
        equation.set("error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


calculator = Tk()
calcFont = ('verdana', 20)
fieldFont = ('verdana', 14)
calculator.configure(background = "light gray")

calculator.title("Simple Calculator")

calculator.geometry("240x250")

equation = StringVar()
calcFrame = Frame(calculator, background = 'dark gray')
calcFrame.grid(column = 0, row = 2)
expression_field = Entry(calculator,textvariable = equation)
expression_field.configure(font = fieldFont)

expression_field.grid(column = 0, row = 1, columnspan = 1)

button1 = Button(calcFrame, text=' 1 ', command=lambda: press(1), width = 3)
button1.configure(font = calcFont)
button1.grid(column=1, row=3)
button2 = Button(calcFrame, text=' 2 ', command=lambda: press(2), width = 3)
button2.configure(font = calcFont)
button2.grid(column=2, row=3)
button3 = Button(calcFrame, text=' 3 ', command=lambda: press(3), width = 3)
button3.configure(font = calcFont)
button3.grid(column=3, row=3)
button4 = Button(calcFrame, text=' 4 ', command=lambda: press(4), width = 3)
button4.configure(font = calcFont)
button4.grid(column=1, row=2)
button5 = Button(calcFrame, text=' 5 ', command=lambda: press(5), width = 3)
button5.configure(font = calcFont)
button5.grid(column=2, row=2)
button6 = Button(calcFrame, text=' 6 ', command=lambda: press(6), width = 3)
button6.configure(font = calcFont)
button6.grid(column=3, row=2)
button7 = Button(calcFrame, text=' 7 ', command=lambda: press(7), width = 3)
button7.configure(font = calcFont)
button7.grid(column=1, row=1)
button8 = Button(calcFrame, text=' 8 ', command=lambda: press(8), width = 3)
button8.configure(font = calcFont)
button8.grid(column=2, row=1)
button9 = Button(calcFrame, text=' 9 ', command=lambda: press(9), width = 3)
button9.configure(font = calcFont)
button9.grid(column=3, row=1)
button0 = Button(calcFrame, text=' 0 ', command=lambda: press(0), width = 3)
button0.configure(font = calcFont)
button0.grid(column=2, row=4)
buttonAdd = Button(calcFrame, text=' + ', command=lambda: press('+'), width = 3)
buttonAdd.configure(font = calcFont)
buttonAdd.grid(column=4, row=4)
buttonSub = Button(calcFrame, text=' - ', command=lambda: press('-'), width = 3)
buttonSub.configure(font = calcFont)
buttonSub.grid(column=4, row=3)
buttonMul = Button(calcFrame, text=' x ', command=lambda: press('*'), width = 3)
buttonMul.configure(font = calcFont)
buttonMul.grid(column=4, row=2)
buttonDiv = Button(calcFrame, text=' / ', command=lambda: press('/'), width = 3)
buttonDiv.configure(font = calcFont)
buttonDiv.grid(column=4, row=1)
buttonCalc = Button(calcFrame, text=' = ', command=lambda: calculate(), width = 3)
buttonCalc.configure(font = calcFont)
buttonCalc.grid(column=3, row=4)
buttonClear = Button(calcFrame, text = 'C', command=lambda: clear(), width = 3)
buttonClear.configure(font = calcFont)
buttonClear.grid(column = 1, row = 4)

calculator.mainloop()

