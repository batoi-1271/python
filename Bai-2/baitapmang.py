import sys
import socket

temp = input("Nhap vao dia chi IP/tenmien: ")
ip = socket.gethostbyname(temp)
print("Vui long doi! Qua trinh quet IP dang duoc tien hanh...")

try:
    for port in range (1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        print("Checking " + ip+ ":" +str(port))
        result = sock.connect_ex((ip, port))
        if result == 0:
            print("Cong {}: dang duoc mo".format(port))
        sock.close()
except KeyboardInterrupt:
    print("An Ctrl+C de thoat!")
    sys.exit()

except socket.error:
    print("Khong ket noi voi may chu.")
    sys.exit()