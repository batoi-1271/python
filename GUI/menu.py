import tkinter as tk
window = tk.Tk()
window.geometry('350x200')
window.title("Menu Basic")

main_menu = tk.Menu(window)

child_menu = tk.Menu(main_menu)
child_menu.add_command(label = 'New project')
child_menu.add_command(label = 'New')
child_menu.add_command(label = 'New scratch file')
child_menu.add_command(label = 'Open')
child_menu.add_command(label = 'Save as')
child_menu.add_separator()
child_menu.add_command(label = 'Exit')
main_menu.add_cascade(label = 'File', menu= child_menu)

window.config (menu = main_menu)
window.mainloop()