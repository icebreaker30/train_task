inFile, myDict = open("input.txt", encoding="utf8"), {}
i = 0
outFile = open('output.txt', 'w', encoding='utf8')
for line in inFile:
    myDict[line] = myDict.get(line, 0) + 1
    i += 1
inFile.close()
p = (sorted(myDict, key=lambda i: (-myDict[i], i)))
if myDict[p[0]] > i/2:
    print(p[0], file=outFile)
else:
    print(p[0], p[1], sep='\n', file=outFile)
