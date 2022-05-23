from tkinter import *
from random import randint
lineX1 = 0
lineX2 = 100
lineY1 = 0
lineY2 = 100
lineWidth = 5

def randomizer(min,max):
    randomNumber = randint(min,max)
    print(randomNumber)
    return(randomNumber)
lineX1 = randomizer(0,100)
lineY1 = randomizer(0,100)
lineX2 = randomizer(20,200)
lineY2 = randomizer(20,200)
root = Tk()

C = Canvas(root, bg = "light gray", height = 250, width = 300)

line = C.create_line(lineX1, lineY1, lineX2, lineY2, width = lineWidth, fill = "blue")


C.pack()
mainloop()
