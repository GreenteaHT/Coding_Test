# https://school.programmers.co.kr/learn/courses/30/lessons/12914

from math import factorial

# def fac(a, b):
#     alu = 1
#     for i in range(a, b + 1):
#         alu *= i
#     return alu
#
# def solution(n):
#     answer = 0
#     for i in range(0, n//2 + 1):
#         answer += fac(n - i*2 + 1, n - i) // fac(1, i)
#     return answer % 1234567


def solution(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a+b
    return b

# 입출력 예시
print(solution(4))
print(solution(3))



