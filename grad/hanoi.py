def hanoi_func(n):
    if n == 1:
        return 1
    return hanoi_func(n - 1) * 2 + 1

count = 0
def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print(n, a, "->", c)
        hanoi(n-1, b, a, c)
        

# print(hanoi_func(64) // 60 // 60 // 24 // 365)
print(hanoi(5, 1, 2, 3))