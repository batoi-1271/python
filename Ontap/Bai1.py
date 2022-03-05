import math
import random
import shutil
from tkinter import messagebox
from turtle import *
from tkinter import *
import webbrowser as web
import mysql.connector
import socket
import os


def mainMenu():
    print("1. Viết chương trình nhập vào số tự nhiên N bất kỳ từ bàn phím.")
    print("2. Giải và biện luận phương trình")
    print("3. Thực hiện tính tổng giá tiền Taxi")
    print("4. Ghi dữ liệu vào một file cho trước")
    print("5. Tim file va sao chep.")
    print("6: Tao ngoi sao")
    print("7. Dò tìm địa chỉ IP của website")
    print("8. Viết chương trình tạo bảng SinhVien (MaSV, TenSV, NamSinh,GioiTinh, HocPhi) bằng Python có kết nối cơ sở dữ liệu SQL")
    print("9. Cập nhập hoặc xóa một bảng từ cơ sở dữ liệu SQL đã có.")
    print("10. Tạo giao diện nút Button")
    print("11. Hiển thị menu cấp 1 và cấp 2 dạng sổ thư mục")
    print("13. Quit")
    while True:
        try:
            selection = int(input("Enter choice: "))
            if selection == 1:
                bai1()
                break
            elif selection == 2:
                bai2()
                break
            elif selection == 3:
                bai3()
                break
            elif selection == 4:
                bai4()
                break
            elif selection == 5:
                bai5()
                break
            elif selection == 6:
                bai6()
                break
            elif selection == 7:
                bai7()
                break
            elif selection == 8:
                bai8()
                break
            elif selection == 9:
                bai9()
                break
            elif selection == 10:
                bai10()
                break
            elif selection == 11:
                bai11()
                break
            elif selection == 13:
                break
            else:
                print("Invalid choice. Enter 1 - 13")
                mainMenu()
        except ValueError:
            print("Invalid choice. Enter 1 - 13")
    exit


def bai1():
    print("Bai 1: Viết chương trình nhập vào số tự nhiên N bất kỳ từ bàn phím.")
    n = int(input("Nhap so N: "))
    tong = 0
    tongl = 0
    tongc = 0
    print("Day so tu 1 den ", n, "la: ")
    for i in range(1, n+1):
        print(i, end=" ")
    for i in range(1, n+1):
        tong += i
        if i % 2 != 0:
            tongl += i
        elif i % 2 == 0:
            tongc += i
    print("\nTong cac so tu 1 -> ", n, "la: ", tong)
    print("Tong cac so chan tu 1 -> ", n, "la: ", tongc)
    print("Tong cac so le tu 1 -> ", n, "la: ", tongl)
    anykey = input("\nEnter anything to return to main menu: ")
    mainMenu()

def bai2():
    print("Bai 2: Giải và biện luận phương trình")
    print("----------")
    print("\nPhuong trinh : Ax +B =0")
    a = float(input("Nhap he so a: "))
    b = float(input("Nhap he so b: "))
    if a == 0:
        if b == 0:
            print("Phuong trinh co vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co 1 nghiem x = ", -b/a)

    print("----------")
    print("\nPhuong trinh : Ax2 + Bx + C = 0")
    a1 = float(input("Nhap he so a: "))
    b1 = float(input("Nhap he so b: "))
    c1 = float(input("Nhap he so c: "))
    def giaiPTbac2 (a1, b1, c1):
        if a1 == 0:
            if b == 0:
                print("Phuong trinh vo nghiem!")
            else:
                print("Phuong trinh co 1 nghiem x = ", +(-c1/b1))
            return
        delta = b1 * b1 - 4 * a1 * c1;
        if (delta > 0):
            x1 = (float)((-b + math.sqrt(delta)) / (2 * a));
            x2 = (float)((-b - math.sqrt(delta)) / (2 * a));
            print("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2);
        elif (delta == 0):
            x1 = (-b / (2 * a));
            print("Phương trình có nghiệm kép: x1 = x2 = ", x1);
        else:
            print("Phương trình vô nghiệm!");
    giaiPTbac2(a1, b1, c1)
    anykey = input("Enter anything to return to main menu: ")
    mainMenu()

def bai3():
    print("3. Thực hiện tính tổng giá tiền Taxi")
    km = int(input("Nhap so KM: "))
    tien = 0
    if km <= 1:
        print("Don gia: 10.000vnd")
    elif km >=2 and km <=10:
        tien = km * 9000
        print("Don gia:", tien)
    elif km > 11:
        tien = km * 8000
        print("Don gia: ", tien)
    else:
        print("So km khong hop le!!!")
    if tien > 1000000:
        print("Don gia: ", (tien*0.1))
    anykey = input("Enter anything to return to main menu: ")
    mainMenu()

def bai4():
    print("Bai 4: Ghi dữ liệu vào một file cho trước")
    file_open = open("readme.txt", "r+", encoding="utf-8")
    print("Ten cua File la: ", file_open.name)
    # num = int(input("Nhap vi tri ghi de: "))
    # file_open.seek(num)

    data = input("Nhap ND file: ")
    file_open.write(data)
    file_open.close()
    print("Ghi file thanh cong!!!")
    anykey = input("Enter anything to return to main menu: ")
    mainMenu()

def bai5():
    print("5. Tim file va sao chep.")
    tmp = input("Enter your File/Dir: ")
    if not os.path.exists(tmp):
        print(("Not existes"))
    else:
        print("File was existes")
        dst_path = input("Nhap dia chi can copy: ")
        shutil.copyfile(tmp, dst_path)
        print("File copied successfully.")
    anykey = input("Enter anything to return to main menu: ")
    mainMenu()

def bai6():
    print("Bai 6: Tao ngoi sao")
    # color('red', 'green')
    # begin_fill()
    # while True:
    #     forward(150)
    #     left(144)
    #     if abs(pos()) < 1:
    #         break
    # end_fill()
    # done()
    hideturtle()
    penup()
    backward(100)
    pendown()
    n = random.randint(3, 15)
    print(n)
    angle = 180 - 180 / n
    for i in range(n):
        forward(200)
        right(angle)
    anykey = input("Enter anything to return to main menu: ")
    mainMenu()

def bai7():
    print("7. Dò tìm địa chỉ IP của website")
    print("chuong trinh do tim dia chi ip cua 1 website: ")
    domanName = input("Nhap ten mien can kiem tra: ")

    ip = socket.gethostbyname(domanName)

    print("Dia chi IP cua website tren la: ", ip)
    anykey = input("Enter anything to return to main menu: ")
    mainMenu()

def bai8():
    print("Bai 8: ")
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="kinhbac"
    )
    sql = conn.cursor()
    # # sql.execute("CREATE DATABASE kinhbac")
    # sql.execute("show databases")
    for i in sql:
        print(i)
    sql.execute("create table `kinhbac`.`sinhvien_01` (masv int(15) primary key, tenSV varchar(20), namsinh int(4), gioitinh varchar(5), hocphi float(20))")
    sql.execute("SHOW TABLES")
    for i in sql:
        print(i)
    anykey = input("Enter anything to return to main menu: ")
    mainMenu()

def bai9():
    print("Bai 9: ")
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="kinhbac"
    )
    sql = conn.cursor()
    drop_table = "DROP TABLE sinhvien"
    sql.execute(drop_table)
    conn.commit()
    print("Successful delete!!! ")
    anykey = input("Enter anything to return to main menu: ")
    mainMenu()

def bai10():
    print("Bai 10: Tao BUTTON")
    root = Tk()
    root.geometry('300x150')
    root.title("Nguyen Ba Toi")

    frame = Frame(root)
    frame.pack()

    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM)

    def openProgram():
        MsgBox = messagebox.askquestion('Open FB', 'Are you sure you want to open FB',
                                           icon='warning')
        if MsgBox == 'yes':
            web.open("https://fb.com")
        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')
    def endProgram():
        root.destroy()

    hello_Btn = Button(frame, text="Hello", font=('SimSun', 15), command=openProgram)
    hello_Btn.pack(side=LEFT, ipadx=20, pady=50)
    exit_Btn = Button(frame, text="Exit", font=('SimSun', 15), fg='green', command=endProgram)
    exit_Btn.pack(side=LEFT, ipadx=20, pady=50)

    root.mainloop()
    anykey = input("Enter anything to return to main menu: ")
    mainMenu()

def bai11():
    print("Bai 11: ")
    anykey = input("Enter anything to return to main menu: ")
    mainMenu()


#Main routine
mainMenu()

