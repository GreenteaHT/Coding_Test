# https://school.programmers.co.kr/learn/courses/30/lessons/181936

def solution(number, n, m):
    return int(number % n == 0 and number % m == 0)

# 입출력 예시
print(solution(60, 2, 3))
print(solution(55, 10, 5))