def pfound(cur_rel, top,decay):
    sum = cur_rel[0]
    p = [1] * top
    for i in range(1,top):
        p[i] = p[i-1] * (1 - cur_rel[i-1]) * decay
        sum += cur_rel[i] * p[i]
    return(sum)

print(pfound([0.8, 0.2, .6], 3, 0.85))