def solution(sizes):
    for s in sizes:
        s.sort()
    answer = 1
    for i in zip(*sizes):
        answer *= max(i)
    return answer


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

s = solution(sizes)
print(s)
