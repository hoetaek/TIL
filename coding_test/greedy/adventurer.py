# N = int(input("모험가 수"))
# fear_rate = list(map(int, input("공포도 값").split()))

N = 5
fear_rate = [2, 3, 1, 2, 2]

fear_rate.sort()
group_num = 0

count = 0
for member in fear_rate:
    count += 1
    if member <= count:
        count = 0
        group_num += 1

print(group_num)