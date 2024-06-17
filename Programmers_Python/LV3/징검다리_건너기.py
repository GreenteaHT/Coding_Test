# https://school.programmers.co.kr/learn/courses/30/lessons/64062

from collections import deque

def solution(stones, k):
    deq = deque()
    max_values = []

    # 초기 윈도우 설정
    for i in range(k):
        # 자기보다 낮은 인덱스의 값이 낮으면 의미가 없다
        # 이렇게 가장 왼쪽에는 윈도우내에서 가장 큰 값의 인덱스가 유지 된다.
        while deq and stones[i] >= stones[deq[-1]]:
            deq.pop()
        deq.append(i)

    # 첫 윈도우의 최대값 추가
    max_values.append(stones[deq[0]])

    # 슬라이딩 윈도우 처리
    for i in range(k, len(stones)):
        # 만료된 인덱스 제거
        while deq and deq[0] <= i - k:
            deq.popleft()
        while deq and stones[i] >= stones[deq[-1]]:
            deq.pop()
        deq.append(i)
        max_values.append(stones[deq[0]])

    return min(max_values)

# 테스트
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))  # 3

## 바이너리 풀이
# # mid 만큼 건널 수 있는 돌의 개수가 연속으로 k가 나오는지 확인
# def can_cross(stones, k, mid):
#     cnt = 0
#     for stone in stones:
#         if stone - mid < 0:
#             cnt += 1
#             if cnt == k:
#                 return False
#         else:
#             cnt = 0
            
#     return True

# def solution(stones, k):
#     left, right = 1, max(stones)
#     answer = 0
    
#     while left <= right:
#         mid = (left + right) // 2
#         if can_cross(stones, k, mid):
#             answer = mid
#             left = mid + 1
#         else:
#             right = mid - 1
    
#     return answer