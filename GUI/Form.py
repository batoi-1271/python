# import  tkinter as tk
# from tkinter import messagebox
#
# def message():
#     if r.get()==1:
#         messagebox.showinfo("Information", "Ban da lua chon hoc Python")
#     else:
#         messagebox.showinfo("Information", "Ban da lua chon hoc Ruby")
# window = tk.Tk()
# label = tk.Label(text = "Ban lua chon ngon ngu nao \n sau day:", font = "Times 15 bold italic", width = 20)
# label.pack()
# r = tk.IntVar()
# radioButton1 = tk.Radiobutton(text = "Python", variable = r, value = 1, command = message)
# radioButton1.pack(anchor = tk.W)
#
# radioButton2 = tk.Radiobutton(text = "Ruby", variable = r, value = 2, command = message)
# radioButton2.pack(anchor = tk.W)
# window.mainloop()

import tkinter as tk
import tkinter.scrolledtext as tkst
form = tk.Tk()
form.title("giao dien")
form.geometry("300x300")
txt = tkst.ScrolledText(form,width=40,height=10)
txt.pack()
form.mainloop()