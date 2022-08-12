def solution(str1, str2):
    s1 = list(two_str(str1.lower()))
    s2 = list(two_str(str2.lower()))

    inter_set = set(s1) & set(s2)
    inter = []
    for i in inter_set:
        inter.extend([i]*min(s1.count(i), s2.count(i)))
    union = s1 + s2
    for i in inter:
        union.remove(i)
    if not union:
        return 65536

    return int(len(inter) / len(union) * 65536)


def two_str(string: str):
    for i in range(len(string) - 1):
        if string[i:i+2].isalpha():
            yield string[i:i+2]


str1 = "FRANCE"
str2 = "french"
str1 = ""
str2 = "shake hands"
str1 = "aaa"
str2 = "aaaaa"
str1 = "BAAAA"
str2 = "AAA"
# str1 = "aa1+aa2"
# str2 = "AAAA12"
# str1 = "E=M*C^2"
# str2 = "e=m*c^2"

s = solution(str1, str2)
print(s)
