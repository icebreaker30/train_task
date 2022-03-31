class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = 0
        nonzero = 0
        while zero != len(nums) and nonzero != len(nums):
            if nums[zero] != 0:
                zero += 1
            else:
                if nonzero > zero and nums[nonzero] != 0:
                    nums[zero], nums[nonzero] = nums[nonzero], nums[zero]
                nonzero += 1
