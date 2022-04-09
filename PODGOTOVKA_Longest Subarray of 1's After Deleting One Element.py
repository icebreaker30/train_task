class Solution:
    def longestSubarray(self, nums):
        first_zero =  -1
        second_zero = -1
        _max = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if first_zero >= 0 :
                    second_zero = first_zero
                    first_zero = i
                else:
                    first_zero = i
            _max = max(_max, i - second_zero - 1)
        return _max
nums = [0,1,1,1,0,1,1,0,1]
a = Solution()
print(a.longestSubarray(nums))