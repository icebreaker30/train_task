a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = a[0]
n = a[1]
pref = [0] * (len(b) + 1)
for i in range(1, len(b) + 1):
    pref[i] = pref[i -1] + b[i-1]
print(pref)
d = []
e = []
for i in range(n):
    c = list(map(int, input().split()))
    d .append(c[0] - 1)
    e.append(c[1])
print(d)
print(e)
for i in range(len(d)):
    lev = pref[d[i]]
    prav = pref[e[i]]
    print(prav - lev)


