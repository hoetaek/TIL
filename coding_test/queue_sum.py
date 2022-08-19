from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    if sum(q1+q2) % 2 != 0:
        return -1
    target = sum(q1+q2) // 2
    p = 0
    sq = sum(q1)
    while sq != target and p <= len(q1 + q2):
        if sq < target:
            q2_val = q2.popleft()
            q1.append(q2_val)
            sq += q2_val
        else:
            q1_val = q1.popleft()
            q2.append(q1_val)
            sq -= q1_val
        p += 1
    if p == len(q1 + q2) + 1:
        return -1
    return p


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]
queue1 = [1, 1]
queue2 = [1, 5]

s = solution(queue1, queue2)
print(s)
