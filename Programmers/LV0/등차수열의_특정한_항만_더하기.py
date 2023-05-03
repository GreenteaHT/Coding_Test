# https://school.programmers.co.kr/learn/courses/30/lessons/181931

def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i] == True:
            answer += a + i * d
    return answer

# 입출력 예시
print(solution(3, 4, [true, false, false, true, true]))
print(solution(7, 1, [false, false, false, true, false, false, false]))
