# https://school.programmers.co.kr/learn/courses/30/lessons/42883

from collections import deque

def solution(number, k):
    stack = deque([])
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # 만약 k가 남아있는 경우 뒤에서부터 제거 (deque의 슬라이싱 문제)
    while k > 0:
        stack.pop()
        k -= 1
    
    return ''.join(stack)

# 테스트
print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))