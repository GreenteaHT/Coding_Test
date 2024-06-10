# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    map = [[0] * m for _ in range(n)]
    map[0][0] = 1
    
    for x, y in puddles:
        map[y - 1][x - 1] = -1
    
    for i in range(n):
        for j in range(m):
            if map[i][j] == -1:
                map[i][j] = 0
                continue
            if i > 0:
                map[i][j] += map[i-1][j]
            if j > 0:
                map[i][j] += map[i][j-1]
            map[i][j] %= 1000000007
    
    return map[n-1][m-1]


print(solution(4, 3, [[2, 2]]))