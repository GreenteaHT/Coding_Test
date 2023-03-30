# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    H, W = len(board), len(board[0])
    doll_stk = []
    global answer = 0

    doll_pos_lst = [0] * W
    for i in range(W):
        for j in range(H):
            if board[j][i] != 0:
                doll_pos_lst[i] = j

    for i in moves:
        if doll_pos_lst[i] == 0:
            continue
        elif doll_pos_lst[i] == H-1:
            doll_stk.append(board[i][H-1])
            doll_pos_lst[i] = 0
            chk_dup(i, doll_stk)
        else:
            doll_stk.append(board[i][doll_pos_lst[i]])
            doll_pos_lst[i] += 1
            chk_dup(i, doll_stk)

    def chk_dup(n, stk):
        if len(stk) >= 2:
            if stk[-2] == doll_stk[-1]:
                stk.pop()
                stk.pop()
                answr += 1
        return stk

    return answer

# 입출력 예시
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
