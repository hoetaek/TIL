def solution(numbers, hand):
    keymap = {1: "L", 4: "L", 7: "L", 3: "R", 6: "R", 9: "R"}
    keys = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            ["*", 0, "#"]]

    keys_index = {y: [i, j]
                  for i, x in enumerate(keys) for j, y in enumerate(x)}
    string = ""
    left_hand_position = "*"
    right_hand_position = "#"
    for n in numbers:
        if n in keymap:
            string += keymap[n]
            if keymap[n] == "L":
                left_hand_position = n
            elif keymap[n] == "R":
                right_hand_position = n
        else:
            # 거리 구하기
            left_distance = 0
            for i, j in zip(keys_index[n], keys_index[left_hand_position]):
                left_distance += abs(i - j)

            right_distance = 0
            for i, j in zip(keys_index[n], keys_index[right_hand_position]):
                right_distance += abs(i - j)
            # 거리 더 작은 것 누르기
            if left_distance > right_distance:
                string += "R"
                right_hand_position = n
            elif left_distance < right_distance:
                string += "L"
                left_hand_position = n
            else:
                # 거리 같으면 왼손잡이인지, 오른손잡이인지 판단하여 넣기
                if hand == "left":
                    string += "L"
                    left_hand_position = n
                elif hand == "right":
                    string += "R"
                    right_hand_position = n
    return string


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

s = solution(numbers, hand)
print(s)
