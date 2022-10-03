
s = "15383792389738932"


# sum method
answer = sum([int(i) for i in s])
print(answer)


# add to var
answer = 0
for i in s:
    answer += int(i)
print(answer)


# hashset
hs = {}
answer = 0
for i in s:
    hs[int(i)] = hs.get(int(i), 0) + 1

for k in hs.keys():
    answer += hs[k] * k
print(answer)

print(sum(map(int, list(s))))

# moduler
s = int(s)
answer = 0
while s > 0:
    answer += s % 10
    s = s // 10
print(answer)

