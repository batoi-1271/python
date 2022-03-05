import shutil
import os
# shutil.copy("")
tmp = input("Enter your File/Dir Delete: ")
if not os.path.exists(tmp):
    # os.remove(tmp)
    # print("File/Dir deleted")
    print(("Not existes"))
else:
    #print("File/Dir not exists/")
    os.remove(tmp)
    print("File da bi xoa")
