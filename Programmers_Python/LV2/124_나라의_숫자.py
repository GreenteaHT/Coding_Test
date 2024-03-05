# https://school.programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n % 3] + answer
        n //= 3
    return answer

# 입출력 예시
for i in range(1, 5):
    print(solution(i))