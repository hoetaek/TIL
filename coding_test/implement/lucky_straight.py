N = 123403

def solution(N):
    N = str(N)
    left = N[:len(N)//2]
    right = N[len(N)//2:]
    return 'LUCKY' if sum(map(int, list(left))) == sum(map(int, list(right))) else "READY"

# def solution2(N):
#     sum_value = 0
#     while 
#         sum_value += N % 10
#         N = N // 10
#     right = N[len(N)//2:]
#     return 'LUCKY' if sum(map(int, list(left))) == sum(map(int, list(right))) else "READY"

s = solution(N)
print(s)