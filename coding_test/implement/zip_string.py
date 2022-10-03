def solution(S):
    min_length = 10000000000
    if len(S) == 1:
        return 1
    for size in range(1, len(S)//2 + 1):
        min_length = min(min_length, zip_string(S, size))
    return min_length


def zip_string(S, size):
    count = {}
    re = ""
    L = 0
    for R in range(size, len(S) + 1, size):
        L = R - size
        if S[L:R] not in count:
            if count:
                key = next(iter(count))
                num = count.pop(key)
                re += key if num == 1 else str(num) + key

            count[S[L:R]] = 1
        elif S[L:R] in count:
            count[S[L:R]] = count.get(S[L:R]) + 1
    
    key = next(iter(count))
    num = count.pop(key)
    re += key+ S[R:] if num == 1 else str(num) + key + S[R:]
    return len(re)


def solution2(s):
    if len(s) == 1:
        return 1
    zip_s_nums = [get_zip_len(s, i) for i in range(1, len(s)//2+1)]
        
    return min(zip_s_nums)

def get_zip_len(string, n):
    st = []
    result = ""
    for i in range(0, len(string), n):
        s = string[i: i + n]
        if not st or st[-1] == s:
            st.append(s)
        else:
            if len(st) > 1:
                result += str(len(st)) + st[-1]
                st.clear()
                st.append(s)
            else:
                result += st[-1]
                st.clear()
                st.append(s)
    if len(st) > 1:
        result += str(len(st)) + st[-1]
    else:
        result += st[-1]
    return len(result)


S = "aabbaccc" 
S = "ababcdcdababcdcd" 
S = "abcabcdede" 
s = solution(S)
print(s)