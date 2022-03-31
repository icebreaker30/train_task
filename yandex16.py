n = int(input())
slov = dict()
for i in range(n):
    b = list(map(int, input().split()))
    if b[0] in slov:
        slov[b[0]] += b[1]
    else:
        slov[b[0]] = b[1]
list_keys = list(slov.keys())
list_keys.sort()
for i in list_keys:
    print(i, slov[i])

