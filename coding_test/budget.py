def solution(d, budget):
    s = 0
    d.sort()
    for i in range(len(d)):
        s += d[i]
        if s > budget:
            return i
    return i + 1

    # dp = [0] * 100
    # d.sort()
    # for i in range(1, budget + 1):
    #     dp[i] = dp[i-1]


d = [1, 3, 2, 5, 4]
budget = 9
d = [2, 2, 3, 3]
budget = 10

s = solution(d, budget)
print(s)
