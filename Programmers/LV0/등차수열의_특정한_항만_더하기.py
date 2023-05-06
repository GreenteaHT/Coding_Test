# https://school.programmers.co.kr/learn/courses/30/lessons/181931

def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i] == True:
            answer += a + i * d
    return answer

# 입출력 예시
print(solution(3, 4, [True, False, False, True, True]))
print(solution(7, 1, [False, False, False, True, False, False, False]))
