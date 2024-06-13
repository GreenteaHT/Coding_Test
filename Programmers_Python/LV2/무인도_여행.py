# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque

def solution(maps):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    row, column = len(maps), len(maps[0])
    visited = [[False] * column for _ in range(row)]
    day_list = []

    def bfs(x, y):
        queue = deque([(x, y)])
        day = 0
        while queue:
            xx, yy = queue.popleft()
            if visited[yy][xx]:
                continue
            day += int(maps[yy][xx])
            visited[yy][xx] = True
            for dx, dy in directions:
                nx, ny = xx + dx, yy + dy
                if 0 <= nx < column and 0 <= ny < row and maps[ny][nx] != "X" and not visited[ny][nx]:
                    queue.append((nx, ny))
        return day

    for y in range(row):
        for x in range(column):
            if maps[y][x] == "X" or visited[y][x]:
                continue
            day_list.append(bfs(x, y))

    return sorted(day_list) if day_list else [-1]

# 테스트
print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))