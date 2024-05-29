# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = [0] * (right - left + 1)
    for i in range(left, right + 1):
        answer[i - left] = max(i // n, i % n) + 1
    return answer

# 테스트
print(solution(3, 2, 5))
print(solution(4, 7, 14))
