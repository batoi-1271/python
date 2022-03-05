# # CHƯƠNG 6: LẬP TRÌNH ĐỒ THỊ
# import matplotlib.pyplot as plt
# x = [0,1,2,3,4,5,6,]
# y = [1, 0.25, 0.5, 2, 3, 3.75, 3.5]
# # plt.plot([1, 0.25, 0.5, 2, 3, 3.75, 3.5], "ro:")
# plt.plot(x,y,"m*:")
# plt.xlabel("Mặt hàng", fontsize = 10)
# plt.ylabel("Doanh thu", fontsize = 10)
# plt.title("Biểu đồ doanh thu các mặt hàng.")
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return (x-2) * (x-1) * (x+2)

x_1 = np.linspace(start=-3, stop=3, num=100)
y_1 = f(x_1)

plt.xlim(-3, 3)
plt.ylim(-20, 10)
plt.xlabel("Trục x", font="Tahoma", size=14)
plt.ylabel("Trục y", size=12)
plt.title('bieu do y =(x+2)(x-1)(x-2)')
plt.title("Vũ THị Ngọc Mai")
plt.plot(x_1, y_1, "r")

y = []
x = []
for i in range(-3, 3, 1):
    if f(i) == 0:
        y.append(0)
        x.append(i)

print(x)
print(y)

plt.scatter(x, y, s=30, c = "green")
plt.show()






# plt.plot([1, 0.25, 0.5, 2, 3, 3.75, 3.5
# ], "ro:")
# x = [ 18, 20 , 17, 22, 6, 11]
# y = [2, 3 , 4, 5, 6, 7]
# plt.plot(x, y, "m*", label = "riding")
# x = [ 8,19 , 17, 22]
# y = [7, 8, 9, 10]
# plt.plot(x, y, "ro", label = "Swimming")
# x = [ 35, 40 , 44, 38, 49, 33]
# y = [2, 3 , 4, 5, 6, 7]
# plt.plot(x, y, "b^", label = "Saling")

# riding = ((17, 18, 21, 22, 19, 21, 25, 22, 25, 24),
# (3, 6, 3.5, 4, 5, 6.3, 4.5, 5, 4.5, 4))
# plt.scatter(riding[0], riding[1], c='r', marker='^', label="Riding")
# swimming = ((17, 18, 20, 19, 22, 21, 23, 19, 21, 24),
# (8, 9, 7, 10, 7.5, 9, 8, 7, 8.5, 9))
# plt.scatter(swimming[0], swimming[1], c='b', marker='o', label="Swimming")
#
# sailing = ((31, 28, 29, 36, 27, 32, 34, 35, 33, 39),
# (4, 6.3, 6, 3, 5, 7.5, 2, 5, 7, 4))
# plt.scatter(sailing[0], sailing[1], c='g', marker='*', label="Salling")
#
#
# plt.xlabel("AGe")
# plt.ylabel("Hour")
# plt.title("Activities Scatter Graph")
# plt.legend()

# values = ["python", "PHP", "Javascript", "Kotlin"]
# percent = [45, 30, 15, 10]
# plt.pie(percent, labels=values, autopct="%1.f%%", counterclock=False, startangle=90)

# x = (5, 3, 5, 4, 😎
# y = (129, 230, 95, 77, 165)
#
# plt.scatter(x, y)
#
# z = np.polyfit(x, y, 1)
# p = np.poly1d(z)
# plt.plot(x, p(x), 'r')

# x = np.linspace(0, 20, 100)
# y = np.sin(x)

# plt.plot(y, 'b')
# t1 = y.copy()
# t2 = y.copy()
# t1[t1 <= 0] = np.nan
# t2[t2 >= 0] = np.nan
#
# plt.plot(t1, 'r:')
# plt.plot(t2, 'b:')
# plt.show()


# y[y > 0.5] = 0.5
# y[y <=0.75] = -0.75
# plt.plot(x, y, "r")

# y1 = np.where(y>0.5, 0.5, y)
# y1 = np.where(y1 <-0.75, -0.75, y1)

# plt.plot(y1, 'r')
# plt.show()
