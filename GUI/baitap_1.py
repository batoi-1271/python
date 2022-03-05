from tkinter import *

root = Tk()
root.geometry('300x150')
root.title("Nguyen Ba Toi")

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
def openProgram():
    import Passward

def endProgram():
    root.destroy()

hello_Btn = Button(frame, text = "Hello", font=('SimSun', 15), command = openProgram)
hello_Btn.pack(side=LEFT, ipadx=20, pady=50)
exit_Btn = Button(frame, text = "Exit", font=('SimSun', 15), fg = 'green', command = endProgram)
exit_Btn.pack(side=LEFT, ipadx=20, pady=50)

root.mainloop()