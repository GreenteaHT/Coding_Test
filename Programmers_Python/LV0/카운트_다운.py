# https://school.programmers.co.kr/learn/courses/30/lessons/181899

def solution(start, end):
    return [i for i in range(start, end-1, -1)]

# 입출력 예시
print(solution(10, 3))