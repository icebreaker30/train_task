n = int(input())
sob = []
for i in range(n):
    ot = list(map(int, input().split()))
    sob.append((ot[0], 1))
    sob.append((ot[1], -1))
sob.sort()
online = 0
allpaint = 0
for i in range(len(sob)):
    if online > 0:
        allpaint += sob[i][0] - sob[i-1][0]
    if sob[i][1] == 1:
        online += 1
    else:
        online -= 1
print(allpaint)


