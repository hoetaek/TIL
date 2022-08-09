from itertools import combinations


def solution(orders, course):
    countCourse = {}

    for c in course:
        c_dict = countCourse.get(c, {})

        for person in orders:
            coms = combinations(person, c)
            for com in coms:
                com = "".join(sorted(com))
                c_dict[com] = c_dict.get(com, 0) + 1
        countCourse[c] = c_dict
    answer = []
    for c in course:
        coms = countCourse[c]
        # print(coms)
        s = sorted(coms, key=lambda x: coms[x], reverse=True)
        # print("s[0]", s[0])
        # print("coms[s[0]]", coms[s[0]])
        if not s:
            continue
        max_count = coms[s[0]]

        if max_count >= 2:
            for i in s:
                if coms[i] == max_count:
                    answer.append(i)
                else:
                    break
    answer.sort()
    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
courses = [2, 3, 4]
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# courses = [2, 3, 5]
# orders = ["XYZ", "XWY", "WXA"]
# courses = [2, 3, 4]

s = solution(orders, courses)
print(s)
