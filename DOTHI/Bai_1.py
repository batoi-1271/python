# # import wx
# # # import tkinter as tk
# # window = wx.App()
# # frame = wx.Frame(parent = None, title = "Gui voi thu WX")
# # text = wx.StaticText(parent = frame, label = "Hoc ngon ngu Python")
# # frame.Show()
# # window.MainLoop()

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,100)
y=(x+2)*(x-1)*(x-2)
plt.plot([-2,1,2],[0,0,0], 'ro-')
plt.title('Nguyễn Bá Tới')
plt.xlabel('Trục x')
plt.ylabel('Trục y')
plt.plot(x,y)
plt.show()

import numpy as np
from matplotlib import pyplot as plt
x = np.linspace(-3,3,100)
y = (x+2)*(x-1)*(x-2)
plt.title("Nguyen Gia Truong")
plt.xlabel("Truc X")
plt.ylabel("Truc Y")
plt.plot(x,y,'--r')
listX = [-2, 1, 2]
listY = [0, 0, 0]
plt.scatter(listX, listY)
plt.show()