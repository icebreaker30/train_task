mat = [[1,2],[3,4]]
r = 1
c = 4
temp = []
if len(mat) == c and len(mat[0]) == r:
    print( mat)
else:
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            temp.append(mat[j][i])
len_str = len(temp) / c
for i in range(len_str):
    


    print(temp)