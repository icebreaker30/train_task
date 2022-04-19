a = list(map(int, input().split()))
d = min(a[1], a[2])
e = max(a[1], a[2])
dis = e - d - 1
dis2 = a[0] - e + d - 1
print(min(dis, dis2))

list1 = list(map(int, input().split()))

min1 = min(list1[1],list[2])
max1 = max(list[1],list[2])

dist1 = max1-min1 -1
dist2= list1[0] + min1 - max1 -1


print(min(dist1,dist2))