a = list(map(int, input().split()))
d = min(a[1], a[2])
e = max(a[1], a[2])
dis = e - d - 1
dis2 = a[0] - e + d - 1
f = min(dis, dis2)

if f >= 0:
	print(f)
else:
	print(0)
	