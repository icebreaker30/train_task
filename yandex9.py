a = int(input())
b = list(map(int, input().split()))
t = 0
b.sort()
for i in range(len(b) - 1):
    t += b[i]
print(t)
