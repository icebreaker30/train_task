n = int(input())
l = list(map(int, input().split()))
if len(l) % 2 == 1:
    print(round(l[round(len(l)/2 - 0.5)]))
else:
    print(round((l[round(len(l)/2) - 1] +l[round(len(l)/2 + 1) - 1]) / 2))
