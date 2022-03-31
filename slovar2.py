n = int(input())
mdi = {}
for i in range(n):
    line = list(map(str, input().split()))
    mdi[line[1]] = line[0]
sin = str(input())
for key, mdi[key] in mdi.items():
    if key == sin:
        print(mdi[key])
    elif mdi[key] == sin:
        print(key)
