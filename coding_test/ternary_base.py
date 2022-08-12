def solution(n):
    for i in range(1, 18):
        if n < 3 ** i:
            break
    num_str = ""
    remainder = n
    for j in range(i-1, -1, -1):
        num_str += str(remainder // 3 ** j)
        remainder = remainder % 3 ** j

    answer = 0
    for i in range(len(num_str)):
        answer += int(num_str[i]) * 3 ** i
    return answer


s = solution(125)
print(s)
