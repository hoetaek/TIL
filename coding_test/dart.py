"""
def solution(dartResult):
    li = []
    lastIndex = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit() and dartResult[lastIndex:i]:
            li.append(dartResult[lastIndex:i])
            lastIndex = i
    li.append(dartResult[lastIndex:])
    print(li)
    # cal = []
    # for i in li:
    #     num = i[0]
    #     if i[1] == "D":
    #         num = int(num) ** 2
    #     elif i[1] == "T":
    #         num = int(num) ** 3
    #     else:
    #         num = int(num)
    #     if len(i) == 3:
    #         if i[2] == "*":
    #             print("oh")
    #             cal = list(map(lambda x: x * 2, cal[-2:]))
    #         else:
    #             num = num * -1
    #     cal.append(num)
    # print(cal)
    answer = 0
    return answer
"""
import re


def solution(dartResult):
    answer = 0
    p = re.compile("[0-9]+[SDT][*#]?")
    points = p.findall(dartResult)
    print(points)
    cal = []
    for i in points:

        area_index = i.find("S")
        if area_index == -1:
            area_index = i.find("D")
        if area_index == -1:
            area_index = i.find("T")

        num = i[:area_index]
        if i[area_index] == "D":
            num = int(num) ** 2
        elif i[area_index] == "T":
            num = int(num) ** 3
        else:
            num = int(num)
        if len(i) == area_index + 2:
            if i[area_index + 1] == "*":
                cal[-1:] = cal[-1:] * 2
                num = num * 2
            else:
                num = num * -1
        cal.append(num)
    # print(cal)
    return sum(cal)


"""
def solution(dartResult):
    answer = 0
    index = 0
    num = 0
    cal = []
    for index in range(len(dartResult)):
        c = dartResult[index]
        if c.isdigit():
            num = c
        elif c in ["S", "D", "T"]:
            if c == "D":
                num = int(num) ** 2
            if c == "T":
                num = int(num) ** 3
            cal.append(num)
        else:
            if c == "*":
                cal[-1] = cal[-1] * 2
                cal[-2] = cal[-2] * 2
            if c == "#":
                cal[-1] = cal[-1] * 2
            cal.append(num)

        print(cal)

    return answer
"""

test_cases = [
    {"dart": "1S2D*3T", "r": 37},
    {"dart": "1D2S#10S", "r": 9},
    {"dart": "1D2S0T", "r": 3},
    {"dart": "1S*2T*3S", "r": 23},
    {"dart": "1D#2S*3S", "r": 5},
    {"dart": "1T2D3D#", "r": -4},
    {"dart": "1D2S3T*", "r": 59}
]

for t in test_cases:
    s = solution(t["dart"])
    if s == t["r"]:
        # print("correct")
        pass
    else:
        print("no!")
