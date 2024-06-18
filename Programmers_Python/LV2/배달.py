# https://school.programmers.co.kr/learn/courses/30/lessons/12978

from collections import defaultdict
import heapq

INF = int(1e9)

def solution(N, road, K):
    graph = defaultdict(list)
    heap = [(0, 1)]
    distance = [INF] * (N + 1)
    distance[1] = 0
    
    for e in road:
        graph[e[0]].append((e[2], e[1]))
        graph[e[1]].append((e[2], e[0]))

    # dijkstra 이용
    while heap:
        dis, node = heapq.heappop(heap)
        if distance[node] < dis:
            continue
        
        for v in graph[node]:
            cost = dis + v[0]
            if cost < distance[v[1]]:
                distance[v[1]] = cost
                heapq.heappush(heap, (cost, v[1]))

    return sum(1 for i in distance if i <= K)

# 테스트
print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))