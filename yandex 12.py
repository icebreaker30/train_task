setsize = 10
myset = [[] for _ in range(setsize)]
def add(x):
    myset[x % setsize].append(x)
c = (map(int, input().split()))

d = add(c)
print(d)
