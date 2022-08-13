def isValid(s: str) -> bool:
    st = []
    for i in s:
        if i in ["(", "{", "["]:
            st.append(i)
        elif not st:
            return False
        elif i == ")":
            if st[-1] == "(":
                st.pop()
            else:
                st.append(i)
        elif i == "}":
            if st[-1] == "{":
                st.pop()
            else:
                st.append(i)
        elif i == "]":
            if st[-1] == "[":
                st.pop()
            else:
                st.append(i)

    if st:
        return False
    else:
        return True

def isValid_second(s: str) -> bool:
    st = []
    parentheses_dict = {")":"(", "}":"{", "]":"["}
    for i in s:
        if st and i in parentheses_dict:
            if st[-1] == parentheses_dict[i]:
                st.pop()
            else:
                return False
        else:
            st.append(i)

    if st:
        return False
    else:
        return True

print(isValid_second("(])"))