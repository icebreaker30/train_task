nums = [3,2,4]
target = 6
a = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] + nums[j] == target and i!=j and len(a)==0:
            a.append(i)
            a.append(j)

print(a)