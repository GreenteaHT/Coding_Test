# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque, defaultdict

def bfs(graph, a, b, n):
    queue = deque([a])
    visited = [False] * (n + 1)
    visited[a] = True
    cnt = 0
    
    while queue:
        node = queue.popleft()
        cnt += 1
        for neighbor in graph[node]:
            # 끊어진 노드 만날시 모두 이어진걸로 확인
            if neighbor == b:
                return 8
            
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return cnt

def solution(n, wires):
    graph = defaultdict(list)
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    min_diff = n
    for a, b in wires:
        # 특정 경로 제거
        graph[a].remove(b)
        graph[b].remove(a)

        tree_size = bfs(graph, a, b, n)
        min_diff = min(min_diff, abs((n - tree_size) - tree_size))
        
        # 경로 복구
        graph[a].append(b)
        graph[b].append(a)
        
    return min_diff

# 테스트
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))