nums =[1,2,3,4,0,0,3,2,1,4]


writer = 0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[writer],nums[i] = nums[i], nums[writer]
        writer +=1

print(nums)