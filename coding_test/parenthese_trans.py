def is_correct(p):
    st = []
    
    for i in p:
        if i == "(":
            st.append(i)
        elif i == ")":
            if st and st[-1] == "(":
                st.pop()
            else:
                st.append(i)
    if st:
        return False
    else:
        return True


def inverse_parentheses(p):
    re = ""
    for i in p:
        if i == "(":
            re += ")"
        else:
            re += "("
    return re

parentheses = {"(":1, ")":-1}

def solution(p):
    if not p:
        return ""
    
    s = 0

    for i in range(len(p)):
        s += parentheses[p[i]]
        if s == 0:
            u = p[:i+1]
            v = p[i+1:]
            if is_correct(u):
                return u + solution(v)
            else:
                # 문자열 u가 "올바른 괄호 문자열"이 아니라면
                return "(" + solution(v) + ")" + inverse_parentheses(u[1:-1])




p = "(()())()"
p = ")("
p = "()))((()"
s = solution(p)
print(s)