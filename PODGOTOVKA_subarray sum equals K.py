nums = [1,2,3]
k = 3



res = 0
CurSum = 0
prefixsum = {0:1}
for i in nums:
    CurSum += i
    diff = CurSum - k
    res += prefixsum.get(diff,0)

    prefixsum[CurSum] = 1 + prefixsum.get(CurSum,0)

print(res)