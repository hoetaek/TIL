def solution(N, number):
    limit = min(32000, number * N ** 2)
    dp = []
    for i in range(limit + 1):
        if len(str(i)) == str(i).count(str(N)):
            dp.append(len(str(i)))
        else:
            dp.append(10)
    if N != 1:
        dp[1] = 2
    else:
        dp[1] = 1

    for i in range(2, limit + 1):
        # 1을 더해서 가는 경우
        dp[i] = min(dp[i - 1] + dp[1], dp[i])
        
        if i % N == 0:
            # N을 곱해서 가는 경우
            dp[i] = min(dp[i // N] + 1, dp[i])
        if i - N > 0:
            # N을 더해서 가는 경우
            dp[i] = min(dp[i - N] + 1, dp[i])
        # 1을 빼서 가는 경우
        if i + 1 < limit:
            dp[i] = min(dp[i + 1] + dp[1], dp[i])

        if limit > i * N:
            # N으로 나눠서 가는 경우
            dp[i] = min(dp[i * N] + 1, dp[i])
        # N을 빼서 가는 경우
        if limit > i + N:
            dp[i] = min(dp[i + N] + 1, dp[i])

    for i in range(limit, 1, -1):
        # 1을 더해서 가는 경우
        dp[i] = min(dp[i - 1] + dp[1], dp[i])
        
        if i % N == 0:
            # N을 곱해서 가는 경우
            dp[i] = min(dp[i // N] + 1, dp[i])
        if i - N > 0:
            # N을 더해서 가는 경우
            dp[i] = min(dp[i - N] + 1, dp[i])
        # 1을 빼서 가는 경우
        dp[i] = min(dp[i + 1] + dp[1], dp[i])

        if limit > i * N:
            # N으로 나눠서 가는 경우
            dp[i] = min(dp[i * N] + 1, dp[i])
        # N을 빼서 가는 경우
        if limit > i + N:
            dp[i] = min(dp[i + N] + 1, dp[i])
    return dp[number] if dp[number] <= 8 else -1
        
        
s = solution(2, 18)
print(s)