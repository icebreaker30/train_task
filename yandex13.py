a = list(map(int, input().split()))
b = dict()
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
for key,value in b.items():
    if value == 1:
        print (key, end=' ')
