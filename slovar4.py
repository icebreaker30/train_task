inFile, myDict = open("input.txt"), {}
for line in inFile:
    for i in list(line.split()):
        myDict[i] = myDict.get(i, 0) + 1
inFile.close()
p = (sorted(myDict, key=lambda i: (-myDict[i], i)))
for i in range(len(p)):
    print(p[i])
