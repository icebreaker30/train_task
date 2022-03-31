
points = [[1,1],[-1,1]]
class Solution2(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        points.sort()
        # Space: O(n)
        points[len(points)/2:] = sorted(points[len(points)//2:], key=lambda x, y: y[1] - x[1] if x[0] == y[0] else x[0] - y[0])
        mid = points[0][0] + points[-1][0]
        left, right = 0, len(points) - 1
        while left <= right:
            if (mid != points[left][0] + points[right][0]) or \
               (points[left][0] != points[right][0] and \
                points[left][1] != points[right][1]):
                return False
            left += 1
            right -= 1
        return True


class Solution:
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        import sys
        if len(points) == 0: return True
        s, s_removed = set([]), set([])
        min_x, max_x = sys.maxsize, -sys.maxsize-1
        for [x, y] in points:
            if x<min_x: min_x = x
            if x>max_x: max_x = x
        mirror_x = (min_x+max_x)/2

        for [x, y] in points:
            if x == mirror_x: continue
            if (x, y) in s_removed: continue
            if (2*mirror_x-x, y) in s:
                s.remove((2*mirror_x-x, y))
                s_removed.add((2*mirror_x-x, y))
                s_removed.add((x, y))
            else:
                s.add((x, y))
        return len(s) == 0

reflect = Solution()
print(reflect.isReflected(points))
points.sort()
print(points)
print(points[1:])