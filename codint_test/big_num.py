def solution(number, k):
    start_idx = 1
    while k > 0:
        if start_idx > 0 and number[start_idx - 1] < number[start_idx]:
            number = number[:start_idx-1] + number[start_idx:]
            print(number)
            k = k - 1
            start_idx = start_idx - 1
            continue

        if start_idx == len(number) - 1:
            number = number[:-1]
            k = k - 1
            start_idx = start_idx + 1

        start_idx = start_idx + 1
        print(start_idx)
    return number


number = "1924"
k = 2
number = "1231234"
k = 3
number = "4177252841"
k = 4
# number = "4321"
# k = 1
print(solution(number, k))
