# https://school.programmers.co.kr/learn/courses/30/lessons/181829

def solution(board, k):
    answer = 0
    for i in range(min(k+1, len(board))):
        for j in range(min(k+1, len(board[0]))):
            if i + j <= k:
                answer += board[i][j]
            else:
                break
    return answer
    # return sum(board[i][j] for i in range(len(board)) for j in range(len(board[0])) if i + j <= k)

print(solution([[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]], 2))