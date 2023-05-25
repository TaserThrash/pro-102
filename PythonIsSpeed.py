
import os
import shutil

a = "C:/Users/Taser/Documents/byjus coding/yesyesyesyesyesyes"
destination = "C:/Users/Taser/Documents/byjus coding/yesyesyesyesyesyes/"
fileList = os.listdir()

print(fileList)

for file in fileList:
    name, extension = os.path.splitext(file)

    if extension == "":
        continue

    if extension == ".xlsx":
        path1 = a + "/" + file
        path2 = destination + "EXCEL"
        path3 = destination + "EXCEL" + "/" + file

        if os.path.exists(path2):
            print("moving" + file)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving" + file)
            shutil.move(path1, path3)

    elif extension == ".docx":
        path1 = a + "/" + file
        path2 = destination + "WORD"
        path3 = destination + "WORD" + "/" + file

        if os.path.exists(path2):
            print("moving" + file)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving" + file)
            shutil.move(path1, path3)
    elif extension == ".txt":
        path1 = a + "/" + file
        path2 = destination + "TEXT"
        path3 = destination + "TEXT" + "/" + file

        if os.path.exists(path2):
            print("moving" + file)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving" + file)
            shutil.move(path1, path3)
    elif extension == ".pdf":
        path1 = a + "/" + file
        path2 = destination + "PDF"
        path3 = destination + "PDF" + "/" + file

        if os.path.exists(path2):
            print("moving" + file)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving" + file)
            shutil.move(path1, path3)
