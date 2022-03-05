from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('350x200')
root.title("CheckButton")
label = Label(root, text='Ban lua chon ngon ngu nao: ', font=('SimSun', 15))
label.pack(pady=10)

v = IntVar(root)
def message():
    if v.get() == 1:
        print("Python")
    elif v.get() == 2:
        print("Java")
    else:
        print("PHP")
c_btn1 = Checkbutton(root, text = "Python", var = v, onvalue = 1, offvalue = 0, command = message, font=('SimSun', 15))
c_btn1.pack(anchor=W)
c_btn2 = Checkbutton(root, text = "Java", var = v, onvalue = 2, offvalue = 0, command = message, font=('SimSun', 15))
c_btn2.pack(anchor=W)
c_btn3 = Checkbutton(root, text = "PHP", var = v, onvalue = 3, offvalue = 0, command = message, font=('SimSun', 15))
c_btn3.pack(anchor=W)

send_Btn = Button(root, text="Send", font=('SimSun', 15))
send_Btn.pack()
root.mainloop()