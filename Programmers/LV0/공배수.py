# https://school.programmers.co.kr/learn/courses/30/lessons/181936

def solution(number, n, m):
    # 조건을 만족 하면 1을 반환, 만족 하지 못하면 0을 반환
    return int(number % n == 0 and number % m == 0)

# 입출력 예시
print(solution(60, 2, 3))
print(solution(55, 10, 5))