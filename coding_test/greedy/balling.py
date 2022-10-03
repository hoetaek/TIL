from itertools import combinations

def solution(N, M, li):
    count = 0
    for i, j in combinations(li, 2):
        if i != j:
            count += 1

    return count


s = solution(5, 3, [1, 3, 2, 3, 2])
s = solution(8, 3, [1, 5, 4, 3, 2, 4, 5, 2])
print(s)