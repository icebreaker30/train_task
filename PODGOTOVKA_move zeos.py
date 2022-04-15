class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        r =0
        while r < (len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

            r += 1

        return nums

nums = [0,1,0,3,12]

clas = Solution()
print(clas.moveZeroes(nums))