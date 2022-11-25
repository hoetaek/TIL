
def solution(n:int, info: list):
    answer = [0] * n
    
    score_diff = 0
    ryan_cost = []

    for idx, num in enumerate(info):
        score = 10 - idx
        if num > 0:
            score_diff -= score
            score *= 2
        cost = num + 1
        ryan_cost.append(((-1 * score / cost, -idx), score, cost, idx))
    print(ryan_cost)
    arrows_left = n
    # while arrows_left > 0 and ryan_cost:
    #     _, score, cost, idx = heapq.heappop(ryan_cost)
    #     print(_, score, cost, idx)
    #     if arrows_left >= cost:
    #         arrows_left -= cost
    #         score_diff += score
    #         answer[idx] = cost
    #     print(arrows_left)
    # print(ryan_cost)
    return answer

    
def calculate_score_diff(info, new_info):
    score_diff = 0
    for idx, (i, j) in enumerate(zip(info, new_info)):
        if i > 0 or j > 0:
            score = (10 - idx) * (1 if i - j < 0 else -1)
            score_diff += score
    return score_diff

info = [0,0,1,2,0,1,1,1,1,1,1]
info = [2,1,1,1,0,0,0,0,0,0,0]
info = [0,0,0,0,0,0,0,0,3,4,3]
new_info = [1,1,2,0,1,2,2,0,0,0,0]

# s = calculate_score_diff(info, new_info)
# print(s)

s = solution(10, info)
