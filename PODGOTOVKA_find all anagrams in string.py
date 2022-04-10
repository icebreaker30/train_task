class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if len(p) > len(s): return []

        hashS = dict()
        hashP = dict()

        for i in range(len(p)):
            hashP[p[i]] = hashP.get(p[i], 0) + 1
            hashS[s[i]] = hashS.get(s[i], 0) + 1

        res = [0] if hashP == hashS else []

        l = 0

        for r in range(len(p), len(s)):
            hashS[s[r]] = hashS.get(s[r], 0) + 1
            hashS[s[l]] -= 1

            if hashS[s[l]] == 0:
                hashS.pop(s[l])

            l += 1

            if hashS == hashP: res.append(l)

        return res