def solution(s):
    times = 0
    total = 0
    while s != "1":
        times += 1
        s, zero_num = remove_zero(s)

        print(s)
        total += zero_num
        s = con2digit(len(s))

        print(s)

        if times > 10:
            break

    answer = [times, total]
    return answer

def remove_zero(s):
    res = ""
    zero_num = 0
    for i in s:
        if i == "0":
            zero_num += 1
            continue
        res += i
    return res, zero_num

def con2digit(n: int):
    res = ""

    while n:
        remainder = n % 2
        n = n // 2
        res = str(remainder) + res

    return res

s = solution("110010101001")
print(s)