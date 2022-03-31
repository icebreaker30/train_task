class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        point1 = 0
        point2 = 0
        result = []
        while point1 < len(nums1) and point2 < len(nums2):
            if nums1[point1] == nums2[point2]:
                result.append(nums1[point1])
                point1 += 1
                point2 += 1

            elif nums1[point1] < nums2[point2]:
                point1 += 1
            else:
                point2 += 1
        return result