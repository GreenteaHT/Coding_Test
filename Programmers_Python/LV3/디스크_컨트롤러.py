# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq
from collections import deque

def solution(jobs):
    jobs.sort()
    n = len(jobs)
    total_time, time = 0, 0
    i = 0
    heap = []
    
    while i < n or heap:
        while i < n and jobs[i][0] <= time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))  # (소요시간, 요청시간)
            i += 1
        if heap:
            job = heapq.heappop(heap)
            time += job[0]
            total_time += time - job[1]
        else:
            time = jobs[i][0]
    
    return total_time // n

# 테스트
print(solution([[0, 3], [1, 9], [2, 6]]))  # 9