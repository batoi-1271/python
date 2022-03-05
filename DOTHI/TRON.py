# import  matplotlib.pyplot as plt
# values = ["Python", "Ruby", "Java", "C"]
# percent = [45, 30, 15, 10]
# colors = ["Gold", "MediumBlue", "SpringGreen", "Red"]
# plt.bar(values, percent)
# plt.xlabel('Names')
# plt.ylabel('Percent')
# plt.title("QUY MO VA CO CAU CAC NGON NGU")
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# x = (5, 5.5, 6, 6.5, 7, 8, 9, 10)
# y = (120, 115, 100, 112, 80, 85, 69, 65)
#
# plt.scatter(x, y)
# z = np.polyfit(x, y, 1)
# p = np.poly1d(z)
# plt.plot(x, p(x), "r")
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(0,20,100)
# y = np.sin(x)
# y2 = []
# for i in y:
# 	if i > 0:
# 		y2.append(0)
# 	elif i < 0:
# 		y2.append(0)
# 	else:
# 		y2.append(i)
# plt.plot(y,"g")
# plt.plot(y2,"r")
#

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,20,100)
y = np.sin(x)
plt.plot(x[y > 0], y[y > 0], "go")
plt.plot(x[y <= 0 ], y[y <= 0], "ro")

plt.xlabel("X", font = "Tahoma", size = 14)
plt.ylabel("Y", size = 12)
plt.title("Bieu do y = sin(x)")

# y[y > 0.5] = 0.5
# y[y < -0.75] = -0.75
# plt.plot(x, y, "r")
plt.show()
