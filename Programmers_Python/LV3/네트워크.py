# https://school.programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

def solution(n, computers):
    networks = 0
    visited = set()
    
    # BFS로 확인하지 않은 네트워크 탐색        
    def bfs(start):
        queue = deque([start])
        while queue:
            node = queue.popleft()
            # 방문한 노드면 queue에서 새로운 노드 확인
            if node in visited:
                continue
            visited.add(node)
            
            # 아직 탐색하지 않은 이어진 노드 기록 
            for i in range(n):
                if computers[node][i] == 1 and i not in visited:
                    queue.append(i)
    
    # 모든 노드를 시작점으로 체크     
    for i in range(n):
        if i not in visited:
            bfs(i)
            networks += 1
        
    return networks

# 테스트
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 출력: 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 출력: 1
