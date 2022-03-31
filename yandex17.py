file, d = open("input.txt"), {}
for line in file:
    a = list(line.split())
    if len(a) == 0:
        break
    else:
        if a[0] in d:
            d[a[0]] += int(a[1])
        else:
            d[a[0]] = int(a[1])
k = list(d.keys())
k.sort()
for i in k:
    print(i, d[i])
