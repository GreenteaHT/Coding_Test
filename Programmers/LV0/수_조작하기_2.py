# https://school.programmers.co.kr/learn/courses/30/lessons/181925?language=python3

def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        a = numLog[i+1] - numLog[i]
        if a == 1:
            answer += 'w'
        elif a == -1:
            answer += 's'
        elif a == 10:
            answer += 'd'
        elif a == -10:
            answer += 'a'
    return answer

# 입출력 예시
print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))
