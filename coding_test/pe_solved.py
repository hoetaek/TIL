def solution(n, lost, reserve):
    lost_ = [l for l in lost if l not in reserve]
    reserve_ = [r for r in reserve if r not in lost]
    students = [
        -1 if i in lost_ else 1 if i in reserve_ else 0 for i in range(1, n + 1)]
    for i, s in enumerate(students):
        if i-1 >= 0 and s + students[i-1] == 0:
            students[i] = 0
            students[i-1] = 0
    return students.count(0) + students.count(1)
