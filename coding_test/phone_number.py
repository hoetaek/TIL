l = ["119", "1195524421"]
hs = {}

idx = 0
m = max(l)
while idx < len(m):
    for i in l:
        if idx < len(i):
            hs[i] = hs.get(i, "") + i[idx]
        else:
            values = hs.values()
            if values != set(values):
                print(False)
    print(hs)
    idx += 1