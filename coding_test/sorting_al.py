def sel_sort(target_li):
    idx = 0
    while idx < len(target_li):
        minIdx = idx
        for i in range(idx, len(target_li)):
            if target_li[i] < target_li[minIdx]:
                minIdx = i
        target_li[minIdx], target_li[idx] = target_li[idx], target_li[minIdx]
        idx += 1
    return target_li


def insertion_sort(target_li: list):
    for i in range(1, len(target_li)):
        now_val = target_li[i]
        idx = i - 1
        while idx >= 0 and target_li[idx] > now_val:
            target_li[idx], target_li[idx + 1] = target_li[idx + 1], target_li[idx]
            idx -= 1
            print(idx)
    return target_li


import random
from turtle import hideturtle


def quick_sort(target_li: list):
    if not target_li:
        return target_li
    ran_idx = random.randint(0, len(target_li) - 1)
    pivot = target_li[ran_idx]
    left_li = []
    right_li = []
    for i in target_li[:ran_idx] + target_li[ran_idx + 1 :]:
        if i <= pivot:
            left_li.append(i)
        else:
            right_li.append(i)
    return quick_sort(left_li) + [pivot] + quick_sort(right_li)


def quick_sort_second_ver(target_li: list):
    if not target_li:
        return target_li
    ran_idx = random.randint(0, len(target_li) - 1)
    pivot = target_li[ran_idx]
    sort_li = []
    li = target_li[:ran_idx] + target_li[ran_idx + 1 :]
    pivot_idx = 0
    for i in range(len(li)):
        if li[i] <= pivot:
            sort_li.insert(0, li[i])
            pivot_idx += 1
        else:
            sort_li.append(li[i])
    return (
        quick_sort(sort_li[:pivot_idx]) + [pivot] + quick_sort(sort_li[pivot_idx + 1 :])
    )


def quick_sort_third_ver(target_li: list):
    quick_sort(target_li, 0, len(target_li) - 1)
    return target_li


def quick_sort(target_li: list, low, high):
    if low < high:
        pivot = target_li[high]
        last_sorted_idx = low - 1
        for i in range(low, high):
            if target_li[i] <= pivot:
                last_sorted_idx += 1
                target_li[last_sorted_idx], target_li[i] = (
                    target_li[i],
                    target_li[last_sorted_idx],
                )
        target_li[last_sorted_idx + 1], target_li[high] = (
            target_li[high],
            target_li[last_sorted_idx + 1],
        )
        quick_sort(target_li, low, last_sorted_idx)
        quick_sort(target_li, last_sorted_idx + 2, high)


def quick_sort_fourth_ver(target_li: list):
    quick_sort_two_pointers(target_li, 0, len(target_li) - 1)
    return target_li


def quick_sort_two_pointers(target_li: list, low, high):
    if low < high:
        pivot = target_li[high]
        right_index = high - 1
        for i in range(low, high):
            while target_li[right_index] > pivot:
                right_index -= 1
            if target_li[right_index] <= pivot and target_li[i] > pivot:
                target_li[right_index], target_li[i] = target_li[i], target_li[right_index]
            if right_index <= i:
                break
        target_li[high], target_li[i+1] = target_li[i+1], target_li[high]
        quick_sort_two_pointers(target_li, low, i)
        quick_sort_two_pointers(target_li, i+2, high)

li = [8, 4, 2, 7, 5, 11, 6]
print(quick_sort_fourth_ver(li))
# print(li[16])
