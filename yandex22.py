n = int(input())
l = list(map(int,  input().split()))
pref = [0] * (len(l) + 1)
# когда считаю префиксную сумму надо двигать и левую и правую границу,
# а я сейчас двигаю только левую
for i in range(1, len(l) + 1):
    pref[i] = pref[i -1] + l[i-1]
a0=[]
print(pref)
for i in range(len(l)):
    if i == len(l) - 1:
        a0.append(pref[i + 1])
    elif l[i] <=0:
        a0.append(pref[i])
print(a0)
if len(a0) > 1:
    for j in range(1, len(a0)):
        a0[j] = a0[j] - a0[j - 1]
print(max(a0))
