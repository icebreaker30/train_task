file, d = open("input.txt"), {}
for line in file:
    a = list(line.split())
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
it = list(d.items())
it1 = sorted(it, key=lambda x:x[0])
it2 = sorted(it1, key=lambda x:x[1], reverse=True)
for i in it2:
    print(*i[0], sep='')
