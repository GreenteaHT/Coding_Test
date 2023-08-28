# https://school.programmers.co.kr/learn/courses/30/lessons/42586

from math import ceil

def solution(progresses, speeds):
    time_required = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    tmp = time_required[0]
    answer = [0]
    for i in time_required:
        if i > tmp:
            tmp = i
            answer.append(0)
        answer[-1] += 1
    return answer

# 입출력 예시
print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))