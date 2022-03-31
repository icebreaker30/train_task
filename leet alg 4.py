nums = [0,0,1]

l = 0
zero_count = 0
while l != len(nums):
    if nums[l] == 0:
        nums.remove(0)
        zero_count +=1
    l += 1
add = [0]*zero_count
nums += add
print(nums)
