# VIẾT CHƯƠNG TRÌNH, NHẬP MỘT THÔNG TIN TỪ BÀN PHÍM. HÃY GHI THÔNG TIN ĐÓ VÀO FILE readme.txt CÓ SẴN.
#         XUẤT RA MÀN HÌNH THÔNG BÁO LÀ GHI THÔNG TIN THÀNH CÔNG
#         IN RA MÀN HÌNH ND VỪA GHI

file_open = open("readme.txt","r+", encoding="utf-8")
print("Ten cua File la: ", file_open.name)
num = int(input("Nhap vi tri ghi de: "))
file_open.seek(num)

data = input("Nhap ND file: ")
file_open.write(data)
file_open.close()
print("Ghi file thanh cong!!!")

#in DL
with open("readme.txt", "r", encoding="utf-8") as f:
    a = f.read()
    # f.close()
    print("ND file da ghi:\n", (a))
