a = list(map(int, input().split()))
pos = list(map(int, input().split()))
l = a[0]
n = a[1]
an = []
centr = l / 2
d_l = centr - pos[0]
d_r = pos[-1] - centr
c = None
for i in range(len(pos)):
    if centr > pos[i] > centr - 1:
        c = pos[i]
    elif pos[i] <= (centr - 1):
        if centr - pos[i] < d_l:
            d_l = centr - pos[i]
    elif pos[i] >= centr:
        if pos[i] - centr < d_r:
            d_r = abs(centr - pos[i])
for i in range(len(pos)):
    if centr - d_l == pos[i] or pos[i] - d_r == centr:
        an.append(pos[i])
if c is not None:
    print(c)
else:
    print(*an)

