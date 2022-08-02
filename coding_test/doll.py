def solution(board, moves):
    # transpose
    t_board = [list(i) for i in zip(*board)]
    print(board)
    print(t_board)

    st = []
    cnt = 0
    # moves - 1 만큼씩 빼기
    for move in moves:
        print(f"move is {move - 1}")
        line = t_board[move - 1]
        print(f"line is {line}")
        for i in range(len(line)):
            if line[i] != 0:
                print(line[i])
                # stack 만들어서 동일한 게 들어가면 pop 하기
                if st and st[-1] == line[i]:
                    st.pop()
                    cnt += 2
                else:
                    st.append(line[i])
                line[i] = 0
                print(st)
                break

    return cnt


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
s = solution(board, moves)
print(s)
