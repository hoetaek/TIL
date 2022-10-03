S = "K1323KA50C0B7"

def rearrange(S):
    string = []
    sum_num = 0
    for i in S:
        if i.isalpha():
            string.append(i)
        elif i.isdigit():
            sum_num += int(i)
    string.sort(key=lambda x: ord(x))
    return "".join(string) + str(sum_num)
import bisect

def rearrange2(S):
    string = []
    sum_num = 0
    for i in S:
        if 65 <= ord(i) and 122 >= ord(i):
            bisect.insort_left(string, i, key= lambda x: ord(x))
        elif 48 <= ord(i) and 57 >= ord(i):
            sum_num += int(i)
    return "".join(string) + str(sum_num)

s = rearrange2(S)
print(s)