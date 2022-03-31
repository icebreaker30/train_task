prices = [2,1,4]


first = 0
second = 1
if len(prices) < 1:
    print( 0)
while second < len(prices)-1:
    prof = prices[second] - prices[first]
    if prof < 0:
        first += 1
        second += 1

    else:
        second += 1
        cur_prof = prices[second] - prices[first]
        prof = max(prof, cur_prof)
if prof <0:
    print(0)
else:
    print( prof)