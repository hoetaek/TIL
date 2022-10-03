
from itertools import combinations

def solution(N, coins):
    coins.sort()

    for target in range(1, sum(coins) + 1):
        if target in coins:
            continue
        else:
            found = False
            new_li = [i for i in coins if i < target]
            for i in range(2, len(new_li) + 1):
                c = combinations(new_li, i)
                c = list(map(sum, c))
                if target in c:
                    found = True
                    break
            if not found:
                return target
    return sum(coins) + 1

def solution(N, coins):
    coins.sort()
    target = 1
    for x in coins:
        if target < x:
            break
        target += x
        print(target)
    return target

N = 5
coins = [1, 2, 3, 4, 8]
# 1, 1, 2, 3, 9
s = solution(N, coins)
print(s)