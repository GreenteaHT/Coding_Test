# https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import Counter

def solution(topping):
    left_set = set()
    right_cnt  = Counter(topping)
    
    result = 0
    
    for i in topping[:-1]:
        # 왼쪽 토핑 세트에 토핑의 종류 추가
        left_set.add(i)
        # 오른쪽 토핑 딕셔너리에 지정된 토핑 제거
        right_cnt[i] -= 1
        
        # 오른쪽 특정 토핑 개수가 0이 되면 딕셔너리에서 제거
        if right_cnt[i] == 0:
            del right_cnt[i]
        
        # 왼쪽과 오른쪽 토핑 종류 개수가 같으면 경우 +1
        if len(left_set) == len(right_cnt):
            result += 1
    
    return result

# 입출력 예시
print(solution([1, 2, 1, 3, 1, 4, 1, 2]))  # 출력: 2
print(solution([1, 2, 3, 4]))  # 출력: 0