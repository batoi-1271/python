# a = int(input("Nhap so a: "))
# b = int(input("Nhap so b: "))
# print("Tong a b la: ",a+b)
# print("Hieu a b la: ",a-b)

# Tinh tong so le tu mang nhap tu ban phim
# n = int(input("Nhap so nguyen n: "))
# tongle=0
# for i in range(n):
#     if (i%2 != 0):
#         print(i, end=" ")
#         tongle += i
# print("\nTong cac so le la: ", tongle)

#Ghi ND file tu ban phim/ Kiem tra su ton tai cua file text.txt, neu co hay copy sang o khac
import shutil
#
# file_open = open("readme.txt","r+", encoding="utf-8")
# print("Ten cua File la: ", file_open.name)

# data = input("Nhap ND file: ")
# file_open.write(data)
# file_open.close()
# print("Ghi file thanh cong!!!")
# #in DL
# with open("readme.txt", "r", encoding="utf-8") as f:
#     a = f.read()
#     print("ND file da ghi:\n", (a))

import os
tmp = input("Enter your File check: ")
if not os.path.exists(tmp):
    print(("Not existes"))
else:
    add = input("Nhap vi tri muon paste file: ")
    shutil.move(tmp, add)
    print("Da di chuyen file den: ", add)