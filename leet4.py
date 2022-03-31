nums1 = [4, 7, 9, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3
point_main = n+m - 1
point1 = m - 1
point2 = n - 1
while point2 >= 0 and point1 >= 0:
    if nums1[point1] > nums2[point2]:
        nums1[point_main] = nums1[point1]
        point1 -= 1
    else:
        nums1[point_main] = nums2[point2]
        point2 -= 1
    point_main -= 1
if point2 >= 0:
    nums1[:point2+1] = nums2[:point2+1]
print(nums1)
