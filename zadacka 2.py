a = list(map(int, input().split()))
i = 0
b = []
while i < len(a):
    if a[i] > 0:
        b.append(a[i])
    i += 1
print(min(b))
