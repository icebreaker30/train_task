l = int(input())
m = list(map(int, input().split()))
b = int(input())
c = []
for i in range(len(m)):
    c.append(abs(b - m[i]))
print(m[c.index(min(c))])
