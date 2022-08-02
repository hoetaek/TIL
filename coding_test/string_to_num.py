def solution(string_num_mix):
    num = ""
    num_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    string_num = ""
    for s in string_num_mix:
        if s.isdigit():
            num += s
        else:
            string_num += s
            if len(string_num) >= 3 and string_num in num_dict.keys():
                num += num_dict[string_num]
                string_num = ""
    return int(num)


s = "one4seveneight"
print(solution(s))
