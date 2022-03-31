def merge(a, b):
    c = []
    i = 0
    j = 0
    while i <= len(a) and j <= len(b):
        if i == len(a) and j == len(b):
            return c
        elif i >= len(a):
            c.append(b[j])
            j += 1
        elif j >= len(b):
            c.append(a[i])
            i += 1
        elif a[i] >= b[j]:
            c.append(b[j])
            j += 1
        elif a[i] < b[j]:
            c.append(a[i])
            i += 1
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))
