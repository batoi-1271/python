import shutil
import os
tmp = input("Enter your name Folder: ")
if not os.path.isdir(tmp):
    os.mkdir(tmp)
    print("Folder created")
    file = input("Enter your File move: ")
    if not os.path.exists(file):
        print(("File not existes"))
        print("File copied fall")
    else:
        shutil.copy(file, tmp)
        print("File copied successfully")
else:
    print("Foder existed")