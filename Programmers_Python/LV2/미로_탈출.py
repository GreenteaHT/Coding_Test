# https://school.programmers.co.kr/learn/courses/30/lessons/159993

from collections import deque

def bfs(start, end, maps):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    m, n = len(maps), len(maps[0])
    queue = deque([start])
    visited = [[False] * n for _ in range(m)]
    visited[start[0]][start[1]] = True
    time = 0
    
    while queue:
        # 다음 거리의 모든 경우의 수
        for _ in range(len(queue)):
            x, y = queue.popleft()
            # 목표 지점에 도착 하게 된다면 걸린 시간 반환
            if (x, y) == end:
                return time
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] != "X" and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
        time += 1
    # 도착 할 수 없다면 0을 반환
    return 0
    
def solution(maps):
    m, n = len(maps), len(maps[0])
    for i in range(m):
        for j in range(n):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)
            elif maps[i][j] == "E":
                end = (i, j)
    
    s_to_l = bfs(start, lever, maps)    # 시작 지점에서 레버 찾기
    l_to_e = bfs(lever, end, maps)      # 레버 지점에서 출구 찾기
    
    return s_to_l + l_to_e if s_to_l and l_to_e else -1

# 테스트
print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))