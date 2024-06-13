from collections import deque, defaultdict

def solution(n, edge):
    # 그래프 작성
    graph = defaultdict(list)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    visited = [False] * (n + 1)
    visited[1] = True
    queue = deque([1])
    distances = [0] * (n + 1)  # node 1로 부터 떨어진 거리
    
    # BFS
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    # 가장 멀리 떨어진 노드의 개수
    return distances.count(max(distances))

# 테스트
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))