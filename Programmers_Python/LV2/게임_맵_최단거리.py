# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n, m = len(maps), len(maps[0])
    start = (0, 0)
    end = (n - 1, m - 1)
    # 미리 배열이 주어지는 상황에서는 set을 이용한 탐색보다 효율적임
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True
    
    queue = deque([(start[0], start[1], 1)])
    while queue:
        x, y, move = queue.popleft()
        if (x, y) == end:
            return move
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, move + 1))
    
    return -1

# 테스트
maps = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1]
]
print(solution(maps))   # 11