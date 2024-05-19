# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq

def solution(n, works):
    # 야근 없으면 집에 가자
    if sum(works) <= n:
        return 0

    # 요소를 음수로 넣어 최대 힙 생성
    works = [-work for work in works]
    heapq.heapify(works)
    
    # 제일 잡업략이 많은 작업을 가져와 줄이고 다시 힙에 저장
    for _ in range(n):
        max_work = heapq.heappop(works)
        heapq.heappush(works, max_work + 1)
    
    return sum(work ** 2 for work in works)
    
    
# 입출력 예시
print(solution(4, [4, 3, 3]))   # 출력: 12
print(solution(1, [2, 1, 2]))   # 출력: 6
print(solution(3, [1, 1]))      # 출력: 0