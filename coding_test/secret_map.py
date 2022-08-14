from tkinter.messagebox import RETRY


def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        s = ""
        print(get_binary(i, n))
        print(get_binary(j, n))
        for k, l in zip(get_binary(i, n), get_binary(j, n)):
            if k == "#" or l == "#":
                s += "#"
            else:
                s += " "
        answer.append(s)
    return answer
    # return answer

def get_binary(n, length):
    s = ""
    while n:
        s += "#" if n % 2 == 1 else " "
        n = n // 2
    return " " * (length - len(s)) + s[::-1]

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
s = solution(n, arr1, arr2)
print(s)
