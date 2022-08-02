def solution(lottos, win_nums):

    best_case = 0
    worst_case = 0
    for win_num in win_nums:
        if win_num in lottos:
            best_case += 1
            worst_case += 1
            lottos.remove(win_num)
        else:
            if 0 in lottos:
                best_case += 1
                lottos.remove(0)

    return list(map(lambda x: 6 if x >= 6 else x, [7-best_case, 7-worst_case]))


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
# lottos = [0, 0, 0, 0, 0, 0]
# win_nums = [38, 19, 20, 40, 15, 25]
# lottos = [45, 4, 35, 20, 3, 9]
# win_nums = [20, 9, 3, 45, 4, 35]

print(solution(lottos, win_nums))
