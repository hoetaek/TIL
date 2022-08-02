def solution(n, lost, reserve):
    temp_lost = lost[:]
    temp_reserve = reserve[:]

    for i in lost:
        if i in temp_reserve:
            temp_lost.remove(i)
            temp_reserve.remove(i)

    for num in temp_reserve:
        if num-1 in temp_lost:
            temp_lost.pop(temp_lost.index(num-1))
        elif num+1 in temp_lost:
            temp_lost.pop(temp_lost.index(num+1))

    answer = n - len(temp_lost)
    return answer


n = 5
lost = [2, 4]
reserve = [1, 3, 5]

n = 5
lost = [2, 4]
reserve = [3]

n = 3
lost = [3]
reserve = [1]

print(solution(n, lost, reserve))
