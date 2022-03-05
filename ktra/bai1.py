import turtle
import mysql.connector

def mainMenu():
    print("1. Nhập giá trị của X.")
    print("2. Tạo bảng với MYSQL")
    print("3. Vẽ ngôi sao 3 lớp.")
    print("4. Quit")
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
                break
            else:
                print("Invalid choice. Enter 1 - 4")
                mainMenu()
        except ValueError:
            print("Invalid choice. Enter 1 - 4")
    exit


def bai1():
    print("Bai 1: Nhap gia tri cua X.")
    x = int(input("Nhập giá trị của x: "))

    if x >= 5:
        print("Với x = ", x, "(DK x >= 5), ta được: f(", x, ')= ', 2 * x * x + 5 * x + 9)
    else:
        print("Với x = ", x, "(DK x < 5), ta được: f(", x, ')= ', -2 * x * x + 4 * x - 9)

    anykey = input("\nEnter anything to return to main menu: ")
    mainMenu()

def bai2():
    print("2. Tạo bảng với MYSQL")
    print("----------")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="kinhbac"
    )
    sql = conn.cursor()
    sql.execute("create table `kinhbac`.`NhanVien` (maNV int(15) primary key, tenNV varchar(20), ngaySinh int(15), gioiTinh varchar(5), diaChi varchar(50))")

    insert_data = "INSERT INTO NhanVien(maNV, tenNV, ngaySinh, gioiTinh, diaChi) VALUES (001, 'Do Duy Nam', 1990, 'Nam', 'Ha Noi')"
    sql.execute(insert_data)
    conn.commit()

    update_data = "UPDATE NhanVien SET tenNV = 'Ba Toi', ngaySinh = 2001 WHERE maNV = 001"
    sql.execute(update_data)
    conn.commit()

    anykey = input("Enter anything to return to main menu: ")
    mainMenu()

def bai3():
    print("3. Vẽ ngôi sao 3 lớp.")
    p = turtle.Turtle()
    for i in range(5):
        p.forward(200)
        p.left(216)
    p.end_fill()
    for i in range(5):
        p.forward(240)
        p.left(216)
    p.end_fill()
    for i in range(5):
        p.forward(280)
        p.left(216)
    p.end_fill()
    p.penup()
    turtle.done()
    anykey = input("Enter anything to return to main menu: ")
    mainMenu()

#Main routine
mainMenu()

