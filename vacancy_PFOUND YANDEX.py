n, decay = map(float, input().split())
rel = list(map(float, input().split()))
q = int(input())


def pfound(cur_rel, top, decay):
    sum = cur_rel[0]
    p = [1] * top
    for i in range(1,top):
        p[i] = p[i-1] * (1 - cur_rel[i-1]) * decay
        sum += cur_rel[i] * p[i]
    return sum


for i in range(q):
    req = list(map(int, input().split()))
    before = pfound(rel,req[2],decay)
    rel[req[0]-1], rel[req[1]-1] = rel[req[1]-1], rel[req[0]-1]
    after = pfound(rel,req[2],decay)
    rel[req[0] - 1], rel[req[1] - 1] = rel[req[1] - 1], rel[req[0] - 1]
    print("%.9f" % abs(before - after))
