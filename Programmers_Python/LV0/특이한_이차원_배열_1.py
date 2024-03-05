# https://school.programmers.co.kr/learn/courses/30/lessons/181833

def solution(n):
    return [[0]*i + [1] + [0]*(n-i-1) for i in range(n)]

# 입출력 예시
print(solution(3))
print(solution(6))
print(solution(1))