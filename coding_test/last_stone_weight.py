import heapq
from typing import List
import bisect

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) >= 2:
            prev = stones.pop()
            curr = stones.pop()
            if prev - curr > 0:
                bisect.insort(stones, prev - curr)
        
        stones.append(0)
        return stones[0]


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]

        heapq.heapify(stones)
        while len(stones) >= 2:
            prev = heapq.heappop(stones)
            curr = heapq.heappop(stones)
            if prev - curr > 0:
                heapq.heappush(stones, prev - curr)

        stones.append(0)
        return abs(stones[0])


stones = [2,7,4,1,8,1]
s = Solution().lastStoneWeight(stones)
print(s)
