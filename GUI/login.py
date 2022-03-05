from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Login form",width=20,font = "Times 20 bold italic", fg = 'red')
label_0.place(x=90,y=53)

label_1 = Label(root, text="Name:",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="User ID:",width=20,font=("bold", 10))
label_2.place(x=77,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Pass:",width=20,font=("bold", 10))
label_3.place(x=84,y=230)

entry_3 = Entry(root, show='*')
entry_3.place(x=240,y=230)

show_hide_button = Button(root, text="Show", font=('SimSun', 10)).place(x=380,y=228)

def submit():
    messagebox.showinfo("Message", "Registration form  seccussfully created...")

Button(root, text='Submit',width=20,bg='red',fg='white',font = "Times 10 bold", command = submit).place(x=180,y=300)

root.mainloop()
