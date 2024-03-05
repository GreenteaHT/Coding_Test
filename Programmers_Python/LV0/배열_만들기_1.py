# https://school.programmers.co.kr/learn/courses/30/lessons/181901

def solution(n, k):
    return [i for i in range(k, n + 1, k)]

# 입출력 예시
print(solution(10, 3))
print(solution(15, 5))
