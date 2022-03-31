class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        point_main = n+m -1
        point1 = m - 1
        point2 =n - 1
        if point1 < 0:
            nums1 = nums2
        while point2>=0 and point1>=0:
            if nums1[point1]>nums2[point2]:
                nums1[point_main] = nums1[point1]
                point1 -=1
            else:
                nums1[point_main] = nums2[point2]
                point2-=1

        return nums1

nums1 =[2,0]
m=1
nums2 = [1]
n=1
ob = Solution()
print(ob.merge(nums1,m,nums2,n))