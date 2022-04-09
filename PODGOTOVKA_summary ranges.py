def summaryRanges( nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    res = []
    for i in nums:

        if res and res[-1][1] == i - 1:
            res[-1][1] = i
        else:
            res.append([i, i])
    return [str(x) + "->" + str(y) if x != y else str(x) for x, y in res]
nums = [0,1,2,4,5,7]
print(summaryRanges(nums))