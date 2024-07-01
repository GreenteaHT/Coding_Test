# https://school.programmers.co.kr/learn/courses/30/lessons/68646

import heapq
import time

def solution(a):
    answer = 0
    l_min = a[0]
    n_min = 0
    heap = [(i, n) for n, i in enumerate(a)]
    heapq.heapify(heap)
    for n in range(1, len(a)):
        while n_min < n:
            r_min, n_min = heapq.heappop(heap)
        
        if a[n] < l_min:
            l_min = a[n]
        
        if a[n] > l_min and a[n] > r_min:
            continue
        
        answer += 1
    return answer + 1

# 테스트
print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))


## 양쪽에서 최소값까지 진행하여 찾는 코드
## 최소값을 한번 구하고 a길이 만큼 확인을 해서 속도가 아주 빠름
## heap을 사용하면 n번만큼 꺼내야하므로 속도가 더 느릴 수 밖에없음
# def solution(a):
#     answer = 1
#     M = min(a)
#     for _ in range(2):
#         m = a[0]
#         i = 1
#         while m != M:
#             if m >= a[i]:
#                 m = a[i]
#                 answer += 1
#             i += 1
#         a.reverse()
#     return answer