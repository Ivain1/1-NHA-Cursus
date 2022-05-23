from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry('640x780')

midframe = Frame(root,bg = 'light gray')
midframe.pack(side=TOP)

displayNum = '0'
txt = Entry(midframe, width = 30, text = '0')
txt.grid(column = 1, row = 0, columnspan = 10)

lbl = Label(midframe, width = 5, text = displayNum)
lbl.grid(column = 4, row = 0)

def inserter(num1):
    displayNum = txt.get()
    displayNum1 = str(displayNum) + str(num1)
    txt.configure(text=displayNum1)


button1 = Button(midframe, text=' 1 ', width = 5, height = 2, bg = 'gray', fg = 'white', command = inserter(1))
button1.grid(column = 1, row = 3)
button2 = Button(midframe, text=' 2 ', width = 5, height = 2, bg = 'gray', fg = 'white', command = inserter(2))
button2.grid(column = 2, row = 3)
button3 = Button(midframe, text=' 3 ', width = 5, height = 2, bg = 'gray', fg = 'white', command = inserter(3))
button3.grid(column = 3, row = 3)
button4 = Button(midframe, text=' 4 ', width = 5, height = 2, bg = 'gray', fg = 'white', command = inserter(4))
button4.grid(column = 1, row = 2)
button5 = Button(midframe, text=' 5 ', width = 5, height = 2, bg = 'gray', fg = 'white', command = inserter(5))
button5.grid(column = 2, row = 2)
button6 = Button(midframe, text=' 6 ', width = 5, height = 2, bg = 'gray', fg = 'white', command = inserter(6))
button6.grid(column = 3, row = 2)
button7 = Button(midframe, text=' 7 ', width = 5, height = 2, bg = 'gray', fg = 'white', command = inserter(7))
button7.grid(column = 1, row = 1)
button8 = Button(midframe, text=' 8 ', width = 5, height = 2, bg = 'gray', fg = 'white', command = inserter(8))
button8.grid(column = 2, row = 1)
button9 = Button(midframe, text=' 9 ', width = 5, height = 2, bg = 'gray', fg = 'white', command = inserter(9))
button9.grid(column = 3, row = 1)
button0 = Button(midframe, text=' 0 ', width = 5, height = 2, bg = 'gray', fg = 'white', command = inserter(0))
button0.grid(column = 2, row = 4)
buttonAdd = Button(midframe,text=' + ', width = 5, height = 2, bg = 'gray', fg = 'white', command = inserter('+'))
buttonAdd.grid(column = 4, row = 4)
buttonSub = Button(midframe,text=' - ', width = 5, height = 2, bg = 'gray', fg = 'white', command = inserter('-'))
buttonSub.grid(column = 4, row = 3)
buttonMul = Button(midframe,text=' x ', width = 5, height = 2, bg = 'gray', fg = 'white', command = inserter('*'))
buttonMul.grid(column = 4, row = 2)
buttonDiv = Button(midframe,text=' / ', width = 5, height = 2, bg = 'gray', fg = 'white', command = inserter('/'))
buttonDiv.grid(column = 4, row = 1)



#num1 = txt.get()
#num2 = txt.get()




#def resolve():

def clicked():
    #res = 'error'
    print(displayNum1)
    txt.configure(text = displayNum1)

buttonCalc = Button(midframe,text=' = ', width = 5, height = 2, bg = 'gray', fg = 'white')
buttonCalc.grid(column = 3, row = 4)
#menu = Menu(root)
#item = Menu(menu)
#item.add_command(label='New')
#menu.add_cascade(label='File', menu=item)
#root.config(menu=menu)

#frame = Frame(root)

#frame.pack()
#lbl = Label(root, fg = 'white', bg = 'darkblue', text = "Are you a Geek?")
#lbl.grid(column = 0, row = 0)

#txt = Entry(root, width = 20)
#txt.grid(column =0, row =1)




#btn = Button(root, text = "Calculate",fg = "red", command=clicked)

#btn.grid(column=2,row=1)

#button = Button(frame,text='Geek')
#button.pack()

root.mainloop()