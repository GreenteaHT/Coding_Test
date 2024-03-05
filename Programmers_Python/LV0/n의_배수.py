# https://school.programmers.co.kr/learn/courses/30/lessons/181937

def solution(num, n):
    if num % n == 0:
        return 1
    else:
        return 0

# 입출력 예시
print(solution(98, 2))
print(solution(34, 3))