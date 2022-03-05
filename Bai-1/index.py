language = "Python"
print("Bạn đang học ngôn ngữ " + language)
# n = int(input("Nhap vao so nguyen N: "))

# if(n%2 == 0):
#     for i in range(2, n + 1, 2):
#         print(i, end=" ")
# elif(n%2 == 1):
#     for i in range(1, n + 1, 2):
#         print(i, end=" ")
# print("So chan")
# for i in range(1, n):
#     if i % 2 ==0:
#         print(i, end=" ")
# print()
# print("So le ")
# for i in range(1, n):
#     if i % 2 !=0:
#         print(i, end=" ")
# print()
# print("Bai 2")
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# array = []
# for i in  a:
#     if i % 2 == 0:
#         array.append(i)
#         print(i, end=" ")
# print()
# print(array)

# a = []
# for i in range(n):
#     a.append(int(input('Nhap so thu %d: ' % (i+1))))
# # print("Mang gom cac phan tu la: ")
# # print(a)
# for i in a:
#     print(i, end=" ")
# div = []
# print("\nCac so chan: ")
# for i in a:
#     if i % 2 == 0:
#         div.append(i)
#         print(i, end=" ")
# print("\nMang so chan", div)
#
# for i in range(1, n):
#     print(i, end=" ")
# tong = 0
# tongc = 0
# tongl =0
# for i in range(1, n+1):
#     tong += i
#     if i % 2 == 0:
#         tongc += i
#     elif i % 2 != 0:
#         tongl += i
# print("\nTong cac so tu 1 -> ", n, "la: ", tong)
# print("\nTong cac so chan tu 1 -> ", n, "la: ", tongc)
# print("\nTong cac so le tu 1 -> ", n, "la: ", tongl)
#
# print("\nBai 5")
# tongcl = 0
# a = int(input("Nhap vao so nguyen A: "))
# for i in range(1, a+1):
#     if i % 2 == 0 and i % 5==0:
#         tongcl += i
# print("\nTong ca so chan va chia het cho 5 tu 1 den ", a, "La: ", tongcl)
#

# print("Bai 6")
# n = int(input("Nhap vao so nguyen N: "))
# sum = 0
# for i in range(1,n+1):
#     sum += i*(-1)**(i+1)
# print("Tong = ", sum)
#
# print("Bai 7")
# sum = 0
# x = 1
# for i in range(1,n+1):
#     x*=i
#     sum+=x
# print("Tong = ", sum)
#
# print("Bai 8")
# sum = 0
# x = 0
# for i in range(1,n+1):
#     x+=i
#     sum+=1/x
# print("Tong = ", sum)


# chương trình in tam giác vuông cân
n = int(input("Nhap vao so nguyen N: "))
for i in range(1, n):
    s = ' *' * i
    print(s)

print("Ve tam giac sao vuong can:")
for i in range(0, n):
    for j in range(0, i):
        print("", end="  ");
    for j in range(i, n):
        print(" *", end="");

    print()
