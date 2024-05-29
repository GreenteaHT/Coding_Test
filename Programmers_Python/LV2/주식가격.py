# https://school.programmers.co.kr/learn/courses/30/lessons/42584

from collections import deque

def solution(prices):
    length = len(prices)
    falling_time = [0] * length
    stack = deque()
    
    # 가격이 떨어질때 하나씩 꺼내어 기록
    for i in range(length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            falling_time[j] = i - j
        stack.append(i)
    
    # 끝까지 가격이 떨어지지 않는 경우
    while stack:
        j = stack.pop()
        falling_time[j] = length - j -1
                
    return falling_time

# 테스트
print(solution([1, 2, 3, 2, 3]))  # 출력: [4, 3, 1, 1, 0]