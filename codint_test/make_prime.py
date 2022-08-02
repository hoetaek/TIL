from itertools import combinations
from math import sqrt


def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        if is_prime(sum(i)):
            answer += 1
    return answer


def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


print(solution([1, 2, 7, 6, 4]))


def combination(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


[print(i) for i in combination([1, 2, 7, 6, 4], 3)]
