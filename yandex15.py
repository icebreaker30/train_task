n = int(input())
sv =[]
for i in range(n):
    sv.append(list(input()))
nom = int(input())
nomera = []
for j in range(nom):
    nomera.append(list(input()))
kolvo = []
for i in range(nom):
    co = 0
    for j in range(n):
        if set(sv[j]) <= set(nomera[i]):
            co += 1
    kolvo.append(co)
for i in range(len(kolvo)):
    if kolvo[i] == max(kolvo):
        print(*nomera[i], sep='')


