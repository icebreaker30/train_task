
nums = [-4,-1,0,3,10]
l=0
r = len(nums) - 1
res= [0] * len(nums)

for i in range(len(nums) - 1 , -1, -1):
    if abs(nums[l]) > abs(nums[r]):
        res[i] = nums[l] **2
        l += 1
    else:
        res[i] =nums[r] ** 2
        r -= 1

print(res)
