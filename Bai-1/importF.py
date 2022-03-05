import function
try:
    a = int(input("Nhap gia tri a: "))
    b = int(input("Nhap gia tri b: "))
    print("Tong hai so la: ", function.addition(a, b))
    print("Hieu hai so la: ", function.subtrction(a, b))
    print("Tich hai so la: ", function.multi(a, b))
    print("Thuong hai so la: ", function.division(a, b))
except:
    print("Dinh dang dau vao khong hop le!")