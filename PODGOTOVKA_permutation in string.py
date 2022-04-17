class Solution:
    def checkInclusion(self, s1, s2):
        w, matched = len(s1), 0
        cntr = dict()
        for i in s1:
            cntr[i] = cntr.get(i, 0) + 1
        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1
                if cntr[s2[i]] == 0:
                    matched += 1
            if i >= w and s2[i - w] in cntr:

                if cntr[s2[i - w]] == 0:
                    matched -= 1
                cntr[s2[i - w]] += 1

            if matched == len(cntr):
                return True
        return False
s1 = "ab"
s2 = "eidbaooo"

a = Solution()
print(a.checkInclusion(s1,s2))