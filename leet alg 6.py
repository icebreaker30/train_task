s = "Let's take LeetCode contest"
s = (list(s.split( )))
a =[]
for i in s:
    i = list(i)
    l = 0
    r = len(i) - 1
    while r > l:
        i[r], i[l] = i[l], i[r]
        l += 1
        r -= 1
    a.append(''.join(i))

a = ' '.join(a)
print(a)