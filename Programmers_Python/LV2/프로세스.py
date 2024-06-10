# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    queue = deque([(priority, i) for i, priority in enumerate(priorities)])
    order = sorted(priorities, reverse=True)
    pointer = 0
    
    while queue:
        current_process = queue.popleft()
        if current_process[0] == order[pointer]:
            pointer += 1
            if current_process[1] == location:
                return pointer
        else:
            queue.append(current_process)
            
    return pointer

# 테스트
print(solution([2, 1, 3, 2], 2))        # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5