n = int(input())
d = {}
count = 0
mess = []
for i in range(n):
    a = int(input())
    if a == 0:
        count += 1
        tema = input()
        message = input()
        d[tema] = [count]
    else:
        count += 1
        message = input()
        for key, value in d.items():
            if a in value:
                d[key] += [count]
dl = []
for key, value in d.items():
    dl.append(len(value))
ind_max = dl.index(max(dl))
j = 0
for key, value in d.items():
    if j == ind_max:
        print(key)
    j += 1


