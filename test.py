s1 = 'abc'
cntr ={}
for i in s1:
    cntr[i] = cntr.get(i, 0) + 1

print(cntr)
print(cntr['a'])
