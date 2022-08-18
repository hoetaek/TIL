from itertools import product

# solution 1
def solution(numbers, target):
    return [sum([j*k for j, k in zip(i, numbers)]) for i in product((-1, 1), repeat=len(numbers))].count(target)

def dfs(idx, numbers, target, val):
    if idx == len(numbers):
        if val == target:
            return 1
        return 0
    ret = 0
    ret += dfs(idx+1, numbers, target, val + numbers[idx])
    ret += dfs(idx+1, numbers, target, val - numbers[idx])
    return ret

# solution 2
def solution(numbers, target):
    return dfs(0, numbers, target, 0)

s = solution([1, 1, 1, 1, 1], 3)
# s = solution([4, 1, 2, 1], 4)
print(s)