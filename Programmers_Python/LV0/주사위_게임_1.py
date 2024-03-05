# https://school.programmers.co.kr/learn/courses/30/lessons/181839

def solution(a, b):
    if a % 2 == 1 and b % 2 == 1:
        return a**2 + b**2
    elif (a % 2 == 1) ^ (b % 2 == 1):
        return 2*(a+b)
    else:
        return abs(a-b)

# 입출력 예시
print(solution(3, 5))
print(solution(6, 1))
print(solution(2, 4))

