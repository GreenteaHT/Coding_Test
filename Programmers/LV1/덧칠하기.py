# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    n_painted, answer = 0, 0
    for s in section:
        if s > n_painted:
            n_painted = s + m - 1
            answer += 1
    return answer

# 입출력 예시
print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))
