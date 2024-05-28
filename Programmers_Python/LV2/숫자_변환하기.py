# https://school.programmers.co.kr/learn/courses/30/lessons/154538

from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    queue = deque([(y, 0)])
    visited = set()  # 중복 값은 연산 생략
    
    while queue:
        current, steps = queue.popleft()
        
        # 이 조건을 먼저 만족하는 경우가 최소이기 때문에 바로 반환
        # 사실 steps를 제거하고 while문의 카운터 하나만 두어도 됨
        if current == x:
            return steps
        
        if current in visited:
            continue
        
        visited.add(current)
        
        next_oprations = []
        if current % 3 == 0:
            next_oprations.append(current // 3)
        if current % 2 == 0:
            next_oprations.append(current // 2)
        if current - n >= x:
            next_oprations.append(current - n)
            
        for next_op in next_oprations:
            if next_op >= x:
                queue.append((next_op, steps + 1))
    
    return -1

# 테스트
print(solution(10, 40, 5))  # 출력: 2
print(solution(10, 40, 30)) # 출력: 1
print(solution(2, 5, 4))    # 출력: -1
