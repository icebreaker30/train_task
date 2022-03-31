st = list(input())
rev = st[::-1]
l = (len(st) // 2)
n = 0
if len(st) % 2 == 1:
    for i in range(l + 1, len(st)):
        if st[i] != rev[i]:
            n += 1

elif len(st) % 2 == 0:
    for j in range (l , len(st)):
        if st[j] != rev[j]:
            n += 1
print(n)