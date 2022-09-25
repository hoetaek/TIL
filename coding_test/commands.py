from collections import defaultdict

def solution(commands):
    answer = []

    table = []
    for _ in range(4):
        table.append(["EMPTY"] * 4)
    print(table)
    merge_data = defaultdict(list)
    val_data = defaultdict(list)

    for command in commands:
        method, *params = command.split()
        if method == "UPDATE":
            if len(params) == 3:
                
                x, y, word = params
                x, y = map(int, (x, y))
                print("table before")
                print(table)
                table[x][y] = word
                # update(table, val_data, x, y, word)
                print("table")
                print(table)
                if (x, y) in merge_data:
                    for x1, y1 in merge_data[(x, y)]:
                        update(table, val_data, x1, y1, word)
            elif len(params) == 2:
                val1, val2 = params
                update_val(table, val_data, val1, val2)
        elif method == "MERGE":
            x1, y1, x2, y2 = map(int, params)
            merge(table, merge_data, (x1, y1), (x2, y2))

        elif method == "UNMERGE":
            x, y = map(int, params)
            unmerge(table, merge_data, x, y)
        elif method == "PRINT":
            x, y = map(int, params)
            print("print")
            print(x, y)
            print(table[x][y])
            answer.append(table[x][y])
            for key, value in merge_data.items():
                print(key, value)
    return answer

def update(table, val_data, x, y, val):
    print("table before1")
    print(table[1][1], table[2][1], table[1][2], table[2][2])
    print(x, y)
    
    print("table after1")
    print(table[1][1], table[2][1], table[1][2], table[2][2])
    val_data[val].append((x, y))

def update_val(table, val_data, val1, val2):
    if val1 in val_data:
        for x, y in val_data[val1]:
            table[x][y] = val2

def merge(table, merge_data, key1, key2):
    x1, y1 = key1
    x2, y2 = key2
    
    val1 = table[x1][y1]
    val2 = table[x2][y2]
    val = val1 if val1 != "EMPTY" else val2
    if x1 == 1 and y1 == 1:
        print(1, 1)
        print(val)
        print(val1)
        print(val2)
    if x1 == 2 and y1 == 2:
        print(val)
        print(val1)
        print(val2)

    merged_pos = merge_data[(x1, y1)] + merge_data[(x2, y2)] + [(x1, y1), (x2, y2)]

    for x3, y3 in merged_pos:
        merge_data[(x3, y3)] = merged_pos
        table[x3][y3] = val



def unmerge(table, merge_data, x, y):
    data = table[x][y]
    for x1, y1 in merge_data[(x, y)]:
        merge_data.pop((x1, y1), None)
        table[x1][y1] = "EMPTY"
    merge_data.pop((x, y), None)
    table[x][y] = data

s = solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "PRINT 1 1", "PRINT 1 2", "PRINT 2 1", "PRINT 2 2"])
print(s)