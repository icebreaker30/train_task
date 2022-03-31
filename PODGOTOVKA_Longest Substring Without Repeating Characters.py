
s = ' '
char = set()
l = 0
res = 0
for r in range(len(s)):
    while s[r] in char:
        char.remove(s[l])
        l += 1
    char.add(s[r])
    res = max(res, r - l + 1)
print(res)

a = '123656'
print(a[4])