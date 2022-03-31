
chars = ['a','a']

s = []
l = r = 0
print(len(chars))
while r < len(chars):

    while r < len(chars) and chars[l] == chars[r]:
        r += 1

    s.append(chars[l])

    if l + 1 != r:
        for c in str(r - l):
            s.append(c)
    l = r

chars[:] = s
print(chars)
print(len(s))