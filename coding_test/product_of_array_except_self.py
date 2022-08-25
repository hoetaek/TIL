# leetcode 238
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            answer[i] = answer[i] * prefix
            prefix = prefix * nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i] * postfix
            postfix = postfix * nums[i]
        return answer

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            answer.append(prefix)
            prefix = prefix * nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i] * postfix
            postfix = postfix * nums[i]
        return answer