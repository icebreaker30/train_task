file, d = open("input.txt"), {}
for line in file:
    a = list(line.split())
    zn = int(a[-1])
    name = (a[:-1])
    name = str(' '.join(name))
    if name in d:
        d[name] += zn
    else:
        d[name] = zn
cum = 0
for key,value in d.items():
    cum+=value
chas = cum/450
place = {}
pl = 0
ostatok ={}
for key,value in d.items():
    place[key] = value//chas
    pl += value//chas
    ostatok[key] = (value%chas)
os =sorted(ostatok.items(), key=lambda item: item[1], reverse=True)
if pl<450:
    for i in os:
        place[i[0]] += 1
        pl += 1
        if pl == 450:
            break
for key,value in place.items():
    print(key, round(value))
        # начало новой темы
