def solution(new_id):
    new_id = new_id.lower()
    new_id = ''.join(c for c in new_id if c not in '~!@#$%^&*()=+[{]}:?,<>/ ')
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    if new_id[0] == ".":
        new_id = new_id[1:]
    new_id = new_id[:15]
    if not new_id:
        new_id = "a"
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]

    return new_id


new_id = "z-+.^."
new_id = "=.="
new_id = "123_.def"
new_id = "abcdefghijklmn.p"
print(solution(new_id))
