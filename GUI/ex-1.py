from tkinter import *
import webbrowser as web
import tkinter as tk
from tkinter import messagebox


def openfb():
    messagebox.showinfo("Chu y", "Se mo FB")
    web.open("https://fb.com")
# def message():
window = tk.Tk()
label = tk.Label(text = "Hello World", bg = "green", font = "Times 15 bold italic", fg = "white", height = 10, width = 20)
label.pack()

btn = tk.Button(text = "OK", bg = "red",font = "Times 15 bold italic", fg = "white", height= 2, width = 20,command=openfb)
btn.pack()

# pic = tk.PhotoImage(file = "bg.jpg")
# label2 = tk.Label(image = pic)
# label2.pack()
window.mainloop()