def count_divisor(n):
    cnt = 0
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            cnt += 1
    
    if n ** (1/2) == i and n != i:
        cnt = cnt * 2 - 2
    else:
        cnt = cnt * 2 - 1
    return cnt
# print(4, count_divisor(4))
# print(count_divisor(3))
for i in range(1, 20):
    print(i, count_divisor(i))
# print(1 ** (1/2))