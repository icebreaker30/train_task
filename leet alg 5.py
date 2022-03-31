
nums = [5,25,75]
target = 100


class Solution:
    def twoSum(self, nums, target) :
        start, end = 0, len(nums) - 1

        while start < end:
            sum = nums[start] + nums[end]

            if sum == target:
                break
            elif sum > target:
                end -= 1
            else:
                start += 1

        return [start + 1, end + 1]
