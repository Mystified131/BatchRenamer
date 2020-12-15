
import os

finlst = []

srchstr = "C:\\Users\\mysti\\Desktop\\DreamImages"

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".jpg") :

            finlst.append(str(filepath))

for elem in finlst:

    bstr = elem[:-4] + "_laura_.jpg" 

    os.rename(elem, bstr) 