# import socket
#
# # print("chuong trinh do tim dia chi ip cua 1 website: ")
# # domanName = input("Nhap ten mien can kiem tra: ")
# #
# # ip = socket.gethostbyname(domanName)
# #
# # print("Dia chi IP cua website tren la: ", ip)
# try:
#     n = int(input("Nhap n: "))
#     if n <= 0:
#         exit()
# except:
#     print('Phai nhap so tu nhien')
#     exit()
# a = []
# for i in range(n):
#     a.append(input('Nhap so thu %d: ' % (i+1)))
#
# print(a)
#
# try:
#     m = int(input("Nhap m: "))
#     if m <= 0:
#         exit()
# except:
#     print('Phai nhap so tu nhien')
#     exit()
# b = []
# for j in range(m):
#     b.append(input('Nhap so thu %d: ' % (j+1)))
#
# print(b)
#
# c = []
# for i in a:
#     for j in b:
#         if i == j and i % 2==0:
#             print(c.append(i))
#             print(c)

lenght_a = int(input("So luong phan tu cua mang a: "))
a = []
for i in range(1, lenght_a +  1):
    tmp = int(input("Nhap gia tri phan tu : "))
    a.append(tmp)

lenght_b = int(input("So luong phan tu cua mang b: "))
b = []
for i in range(1, lenght_b +  1):
    tmp = int(input("Nhap gia tri phan tu : "))
    b.append(tmp)

c = []
for i in a:
    for j in b:
        if(i == j and i %2 == 0 and j % 2 == 0):
            c.append(i)


print(c)