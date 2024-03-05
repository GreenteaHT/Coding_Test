# https://school.programmers.co.kr/learn/courses/30/lessons/120878
from math import gcd


def solution(a, b):
    b //= gcd(a, b)
    while not b % 2:
        b //= 2
    while not b % 5:
        b //= 5
    if b == 1:
        return 1
    else:
        return 2


# 입출력 예시
print(solution(7, 20))
print(solution(11, 22))
print(solution(12, 21))
