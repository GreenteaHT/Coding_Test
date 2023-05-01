# https://school.programmers.co.kr/learn/courses/30/lessons/181884

def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i
        if answer > n:
            return answer
    return answer

# 입출력 예시
print(solution([34, 5, 71, 29, 100, 34]	))