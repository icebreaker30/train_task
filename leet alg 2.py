nums = [1,3,5,6]


target = 7

l = 0
r = len(nums) - 1
while r > l:
    m = (r + l) // 2
    if nums[m] >= target:
        r = m
    else:
        l = m + 1
if l == len(nums) - 1:
    l+=1

print(l)
print(len([1]))