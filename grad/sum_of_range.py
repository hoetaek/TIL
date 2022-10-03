
def gouse(n):
    return n * (n + 1) // 2

def for_loop_sum(n):
    return sum([i for i in range(1, n+ 1)])

def for_loop(n):
    sum_n = 0
    for i in range(1, n + 1):
        sum_n += i
    return sum_n

def recursive(target, n=1, sum_num=0):
    sum_num += n
    if n == target:
        return sum_num
    return recursive(target, n+1, sum_num)

def recursive2(n):
    if n == 1:
        return 1
    return recursive2(n-1) + n

def dynamic(n):
    dp = [0]
    for i in range(n + 1):
        dp.append(dp[-1] + i)
    return dp[-1]

def rec(n):
    if n == 1:
        return 7
    return 2 * rec(n - 1) + 3

print(rec(2))

r = recursive(100)
print(r)

r = dynamic(10)
print(r)
