def solution(cap, n, deliveries, pickups):
    deliver_cap = 0
    pic_cap = 0
    answer = 0

    pointer = n - 1

    while pointer >= 0:
        if deliveries[pointer] != 0 or pickups[pointer] != 0:
            
            answer += (pointer + 1) * 2

            second_pointer = pointer
            while second_pointer >= 0:
                if cap - deliver_cap > deliveries[second_pointer]:
                    deliver_cap += deliveries[second_pointer]
                    deliveries[second_pointer] = 0
                else:
                    deliveries[second_pointer] -= (cap - deliver_cap)
                    deliver_cap = cap
                    
                if cap - pic_cap > pickups[second_pointer]:
                    pic_cap += pickups[second_pointer]
                    pickups[second_pointer] = 0
                else:
                    pickups[second_pointer] -= (cap - pic_cap)
                    pic_cap = cap
                    pointer = n - 1
                    break
                second_pointer -= 1
            deliver_cap = 0
            pic_cap = 0
        pointer -= 1

    return answer


s = solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])
# s = solution(2, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])
# s = solution(2, 7, [1, 0], [0, 3, 0, 4, 0])
print(s)