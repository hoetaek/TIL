class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)
        for i in range(2, len(cost)):
            print(i)
            if cost[i - 1] > cost[i - 2]:
                cost[i] += cost[i - 2]
            elif cost[i - 1] <= cost[i - 2]:
                cost[i] += cost[i - 1]
            print(cost[i])
        return cost[-1]


print(Solution().minCostClimbingStairs([0, 0, 1, 1]))
