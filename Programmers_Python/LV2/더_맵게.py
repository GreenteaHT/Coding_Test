# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    
    cnt = 0
    for _ in range(len(scoville) - 1):
        least_hot_scoville = heapq.heappop(scoville)
        second_hot_scoville = heapq.heappop(scoville)
        if least_hot_scoville >= k:
            return cnt
        
        # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
        mixed_food = least_hot_scoville + second_hot_scoville * 2
        # 새로운 음식을 힙에 push
        heapq.heappush(scoville, mixed_food)
        cnt += 1
    
    if heapq.heappop(scoville) >= k:
        return cnt
    return -1

# 입출력 예시
print(solution([1, 2, 3, 9, 10, 12], 7))

# 비고
# 입력값의 특성상 heapq를 사용하지 않고 queue만으로도 풀 수 있음
# mixed_food의 값을 새로운 queue에 저장하면 자동으로 오름차순이 되기 때문