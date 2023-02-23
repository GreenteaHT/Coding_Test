# https://school.programmers.co.kr/learn/courses/30/lessons/120887

def solution(i, j, k):
    answer = 0
    for a in range(i, j+1):
        for b in str(a):
            if k == int(b):
                answer += 1
    return answer

# 입출력 예시
print(solution(1, 13, 1))
print(solution(10, 50, 5))
print(solution(3, 10, 2))