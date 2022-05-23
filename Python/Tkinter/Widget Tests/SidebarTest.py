from tkinter import *

WindowMain = Tk()
WindowMain.config(background="LightGray")
WindowMain.overrideredirect(1)
global isOpening
global isClosing
isOpening = False
isClosing = False

def MainWindow():
    global WindowMain

#MainWindow_size
def Screen_size():
    app_width = 1280
    app_height = 720

    screen_width = WindowMain.winfo_screenwidth()
    screen_height = WindowMain.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    WindowMain.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#Func1
def close(e):
    for x in range(1000, 1200):
    #while x in range(1000,1200):
        Blue.place(x=x, y=0)
        DarkBlue.place(x=x, y=0)
        Blue.update()
        DarkBlue.update()
        #Blue.after(500, Blue.quit)





#Func2
def open(e):
    for x in range(-1200, -1000):
        Blue.place(x=-x, y=0)
        DarkBlue.place(x=-x, y=0)
        Blue.update(1)
        DarkBlue.update(1)
        #Blue.after(500, Blue.quit)







MainWindow()
Screen_size()

#Label1&2
Blue = Label(WindowMain, background="DeepSkyBlue",
             width=70, height=50)
DarkBlue = Label(WindowMain, width=2, height=100,
                 background="DodgerBlue")

Blue.place(x=1200)
DarkBlue.place(x=1200)


#Buttons
Quit = Button(WindowMain, text="Quit", command=quit,
              background="LightSkyBlue").pack()

Move = Button(WindowMain, text="open", command=open,
              background="LightSkyBlue", state=DISABLED).pack()
Undo = Button(WindowMain, text="close", command=close,
              background="LightSkyBlue", state=DISABLED).pack()

Blue.focus()
Blue.bind("<Enter>", open)
Blue.bind("<Leave>", close)

WindowMain.mainloop()