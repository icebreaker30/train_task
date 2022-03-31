inFile, myDict = open("input.txt"), {}
for line in inFile:
    for i in list(line.split()):
        myDict[i] = myDict.get(i, 0) + 1
inFile.close()
print(len(myDict))
print(sorted(myDict, key=lambda i: (-myDict[i], i))[0])
