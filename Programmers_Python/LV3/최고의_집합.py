# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    if n > s:
        return [-1]
    return [s//n] * (n - s%n) + [s//n + 1] * (s%n)

# 테스트
print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))