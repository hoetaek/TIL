from collections import defaultdict
def solution(genres, plays):
    hs = {}
    hs_2 = set()
    
    for i in range(len(genres)):
        hs[genres[i]] = hs.get(genres[i], 0) + plays[i]
    for i in range(len(genres)):
        hs_2.add((i, plays[i], hs[genres[i]]))
    s = sorted(hs_2, key=lambda x: (-x[2], -x[1], x[0]))
    added = {}
    answer = []
    for i in s:
        added[i[2]] = added.get(i[2], 0) + 1
        if added[i[2]] >= 3:
            continue
        answer.append(i[0])
    return answer
    
