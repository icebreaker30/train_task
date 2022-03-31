n = int(input())
zar = list(map(int, input().split()))
res = zar

# нужно найти пересечение встреч для каждого работника двигая указатель (левый на 1, правая идя по всем и т.д.)

A = []
for i in range(n):
    A.append(set(list(map(int, input().split()))))

l = 0

while l < len(A):
    r = l + 1
    while r < len(A) :
        if len(A[l] & A[r]) > 0 and (zar[l] == 1 or zar[r] == 1) and (A[l] & A[r] != {0}):
            res[l] = res[r] = 1
        r += 1
    l += 1
print(*res)