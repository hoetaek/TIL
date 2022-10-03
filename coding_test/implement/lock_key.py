def solution(key, lock):
    possible_keys = generate_all_keys(key)
    for new_key in possible_keys:
        if is_solvable(new_key, lock):
            return True
    return False

def generate_all_keys(key):
    n = len(key)
    for i in range(n):
        for j in range(n):
            pass
    return

def move_key(key, num):
    new_key = []
    for i in key:
        li = [0] * num + i[num:]
        new_key.append(li)

def is_solvable(key, lock):
    for arr in add_two_arrays(key, lock):
        if 2 in arr:
            return False
    return True
    
def add_two_arrays(arr1, arr2):
    n = len(arr1)
    new_arr = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[i].append(arr1[i][j] + arr2[i][j])
    return new_arr

arr1 = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
arr2 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
r = add_two_arrays(arr1, arr2)
print(r)