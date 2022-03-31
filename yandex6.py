a = list(map(int, input().split()))
b = []
for i in range(len(a)):
    if a[i] == 1:
        e = 0
        l = 0
        for j in a[i:]:
            p = None
            if j == 1 or j == 0:
                e += 1
            elif j == 2:
                p = e
                break
        for k in a[i::-1]:
            t = None
            if k == 1 or k ==0:
                l += 1
            elif k == 2:
                t = l
                break
        if p is None:
            b.append(t)
        elif t is None:
            b.append(p)
        else:
            b.append(min(p, t))
print(max(b))