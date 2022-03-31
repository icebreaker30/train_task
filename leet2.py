
def maxSubArraySum(a):
    max_ending_here = 0
    max_so_far = 0

    for i in a:
        max_ending_here = max(0, max_ending_here + i)

        max_so_far = max(max_ending_here, max_so_far)


    return max_so_far


# Driver function to check the above function
a = [-13, -3, -25, -20, 3, -16, -23, -12, -5, -22, -15, -4, -7]
print(maxSubArraySum(a))