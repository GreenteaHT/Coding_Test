# https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    n_r = len(board)
    n_c = len(board[0])
    skill_type = [0, -1, +1]  # type 1 -> 공격, type 2 -> 회복
    matrix = [[0] * (n_c + 1) for _ in range(n_r + 1)]  # 누적값 저장
    
    # 범위 테두리에 값들을 저장
    for type, r1, c1, r2, c2, degree in skill:
        action = skill_type[type] * degree
        matrix[r1][c1] += action
        matrix[r1][c2 + 1] -= action
        matrix[r2 + 1][c1] -= action
        matrix[r2 + 1][c2 + 1] += action
    
    # 행 방향 누적 합
    for i in range(n_r):
        for j in range(1, n_c):
            matrix[i][j] += matrix[i][j - 1]
    
    # 열 방향 누적 합
    for j in range(n_c):
        for i in range(1, n_r):
            matrix[i][j] += matrix[i - 1][j]

    # 남은 건물 확인  
    answer = 0
    for i in range(n_r):
        for j in range(n_c):
            board[i][j] += matrix[i][j]
            if board[i][j] > 0:
                answer +=1
    
    return answer

# 테스트
print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], 
               [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], 
               [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))