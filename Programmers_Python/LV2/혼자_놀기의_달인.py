# https://school.programmers.co.kr/learn/courses/30/lessons/131130

import heapq

def solution(cards):
    group_n = [] 
    opened = set()  # 상자의 개수가 100개 정도 밖에 되지 않으므로 미리 리스트를 만들어 놓는 것이 편함
    for i in range(1, len(cards) + 1):
        if i in opened:
            continue
        
        # 그룹의 개수 확인
        opened_group = set()
        cnt = 0
        while i not in opened_group:
            cnt += 1
            opened_group.add(i)
            i = cards[i - 1]
        
        heapq.heappush(group_n, -cnt)
        opened.update(opened_group)
        
    if len(group_n) < 2:
        return 0
    
    answer = heapq.heappop(group_n) * heapq.heappop(group_n)
    return answer

# 테스트
print(solution([8, 6, 3, 7, 2, 5, 1, 4]))
print(solution([2, 1]))