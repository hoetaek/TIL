s = "02984"

res = int(s[0])

for i in s[1:]:
    i = int(i)
    # res 까지도 1이면 안되는 것!!
    # i > 1 and res > 1
    if i != 0 and i != 1 and res != 0:
        res *= i
    else:
        res += i

print(res)