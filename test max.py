a =[2,3,4,5,6,4,3,2,1,2,'A','A','B','D']
b ={}
for i in a:
    b[i] = b.get(i,0) + 1
print(b)
