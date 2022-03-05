from tkinter import *
root = Tk()
root.geometry('350x200')
root.title("CheckPass")

ask_label = Label(root, text='Enter your password: ', font=('SimSun', 15))
ask_label.pack(pady=10, anchor=W)

ask_entry = Entry(root, font=('SimSun', 15), show='*')
ask_entry.pack(side=LEFT, anchor=N, padx=5, pady=5)

def show_hide():
    if show_hide_button['text'] == 'Show':
        ask_entry.config(show='')
        show_hide_button.config(tex="Hide")
    else:
        ask_entry.config(show='*')
        show_hide_button.config(text='Show')
show_hide_button = Button(root, text="Show", font=('SimSun', 10), command = show_hide)
show_hide_button.pack(side=LEFT, anchor=N, padx=10, pady=5)
root.mainloop()