class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        left = 0
        right = 0
        for char in S:
            if char == "(":
                left += 1
            else:
                if left <= 0:
                    right += 1
                else:
                    left -= 1
        return left+right