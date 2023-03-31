# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    H, W = len(board), len(board[0])
    doll_stk = []
    answer = 0

    doll_pos_lst = []
    for i in range(W):
        for j in range(H):
            if board[j][i] != 0:
                doll_pos_lst.append(j)
                break

    for k in moves:
        pos = k - 1
        if doll_pos_lst[pos] == H:
            continue
        else:
            doll_stk.append(board[doll_pos_lst[pos]][pos])
            doll_pos_lst[pos] += 1
            if doll_stk[-2:-1] == doll_stk[-1:]:
                doll_stk.pop()
                doll_stk.pop()
                answer += 2

    return answer

# 입출력 예시
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))


## 다른 예시
# def solution(board, moves):
#     cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
#     a, s = 0, [0]
#
#     for m in moves:
#         if len(cols[m - 1]) > 0:
#             if (d := cols[m - 1].pop(0)) == (l := s.pop()):
#                 a += 2
#             else:
#                 s.extend([l, d])
#
#     return a
