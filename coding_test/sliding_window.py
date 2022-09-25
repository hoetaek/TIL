
def longestSubarray(nums):
    maxLength = 0

    length = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            length += 1
        else:
            length = 1
        maxLength = max(maxLength, length)

    return length


s = longestSubarray([4, 2, 2, 3, 3, 3])
print(s)