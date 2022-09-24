
S = "01110110110101001100"

zero_num = 0
one_num = 0

flag = None
for i in S:
    if i == "0" and flag != 0:
        flag = 0
        zero_num += 1
    elif i == "1" and flag != 1:
        flag = 1
        one_num += 1

print(min(zero_num, one_num))