a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
c = a & b
print(len(c))