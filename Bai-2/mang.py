# def Input(arr):
#        n = int(input("Nhap vao so nguyen N: "))
#        for i in range(n):
#            arr.append(int(input('Nhap so thu %d: ' % (i + 1))))
# def Output(arr):
#     print("Mang gom cac phan tu la: ")
#     for i in arr:
#         print(i, end=" ")
# def tong (arr):
#     tong = 0
#     for i in arr:
#         tong = tong + i
#     return tong
def Nhap(a):
    n = int(input("Nhap vao so n: "))
    for i in range(n):
        a.append(int((input("Nhap phan tu thu %d: " %(i+1)))))
def Xuat(a):
    print("Mang gom cac phan tu la: ")
    print(a)



