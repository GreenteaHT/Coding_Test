# https://school.programmers.co.kr/learn/courses/30/lessons/131704

from collections import deque

def solution(order):
    stack = deque([])
    pointer = 0
    
    for i in range(1, len(order) + 1):
        stack.append(i)
        
        # 일치하는 경우 다음 택배 확인
        while stack and stack[-1] == order[pointer]:
            stack.pop()
            pointer += 1
    
    return pointer

print(solution([4, 3, 1, 2, 5]))
print(solution([1, 2, 3, 4, 5]))
