def solution1(s):
    zip_nums = []
    for j in range(1, len(s)//2 + 1):
        split_li = [s[i:i+j] for i in range(0, len(s), j)]
        # print(split_li)

        index = 0
        zip_string = ""
        while index < len(split_li):
            index += 1
            last_element = split_li[index - 1]
            duplicate_times = 1
            while index < len(split_li) and last_element == split_li[index]:
                duplicate_times += 1
                index += 1
                last_element = split_li[index - 1]
            if duplicate_times != 1:
                zip_string += str(duplicate_times)
            # print(last_character)
            zip_string += last_element
        # print(zip_string)
        zip_nums.append(len(zip_string))
    print(zip_nums)
    return min(zip_nums)


def solution(s):
    zip_nums = []
    for j in range(1, len(s)//2 + 1):
        split_li = [s[i:i+j] for i in range(0, len(s), j)]
        # print(split_li)

        if len(set(split_li)) != len(split_li):
            index = 0
            zip_num = 0
            while index < len(split_li):
                index += 1
                last_character = split_li[index - 1]
                duplicate_times = 1
                while index < len(split_li) and last_character == split_li[index]:
                    duplicate_times += 1
                    index += 1
                    last_character = split_li[index - 1]
                if duplicate_times != 1:
                    zip_num += len(str(duplicate_times))
                # print(last_character)
                zip_num += len(last_character)
            # print(zip_num)
            zip_nums.append(zip_num)
        else:
            zip_nums.append(len(s))
    return min(zip_nums)


def solution(s):
    zip_nums = []
    # len(s)//2 + 1
    for j in range(1, 2):
        duplicate_times = 1
        zip_num = 0
        z_string = ""
        for i in range(0, len(s), j):
            # print(i)
            if i >= j:
                last_string = s[i-j:i]
                current_string = s[i:i+j]
                print(f"last string is {last_string}")
                print(f"current string is {current_string}")
                if last_string == current_string:
                    duplicate_times += 1
                    print(duplicate_times)
                    if i != len(s) - 1:
                        continue
            print(f"add {len(last_string)} to {zip_num}")
            if duplicate_times != 1:
                print(f"add length of {str(duplicate_times)} to {zip_num}")
                z_string += str(duplicate_times)
                zip_num += len(str(duplicate_times))
                duplicate_times = 1
            z_string += last_string
            zip_num += len(last_string)
            print("-"*7)
        print(z_string)
        zip_nums.append(zip_num)
    return min(zip_nums)


tests_case = [
    {"s": "aabbaccc", "result":	7},
    # {"s": "ababcdcdababcdcd", "result": 9},
    # {"s": "abcabcdede", "result": 8},
    # {"s": "abcabcabcabcdededededede", "result": 14},
    # {"s": "xababcdcdababcdcd", "result": 17},
]

for c in tests_case:
    sol = solution(c["s"])
    correct = sol == c["result"]
    if not correct:
        print(c["s"])
        print(f"answer is {c['result']} not {sol}")
    # else:
    #     print(f"{c['s']} is correct!!")
    print("-"*20)
