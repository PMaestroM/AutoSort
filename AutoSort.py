import os, time

src = "./AutoSort/"
dest = "./Result/"
os.makedirs(src, exist_ok=True)
os.makedirs(dest, exist_ok=True)

fileList = os.listdir(src)
for fileName in fileList:
    date = time.ctime(os.path.getmtime(src+fileName))
    fileNameArr = date.split(" ")
    for checkName in fileNameArr:
        if checkName == '':
            fileNameArr.remove(checkName)
    dirsName = fileNameArr[0]+"_"+fileNameArr[2]+"_"+fileNameArr[1]+"_"+fileNameArr[4]
    os.makedirs(dest+dirsName, exist_ok=True)
    os.rename(src+fileName, dest+dirsName+"/"+fileName)

print("Sort done.")
