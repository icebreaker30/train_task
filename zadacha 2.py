a = list(map(int, input().split()))
b = 0
c = 0
for j in a:
    if j > 0:
        c = j
    for t in a:
        if 0 < t < c:
            c = t
print(c)
