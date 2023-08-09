# https://school.programmers.co.kr/learn/courses/30/lessons/181912

def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        n = int(i[s:s+l])
        if n > k:
            answer.append(n)
    return answer

# 입출력 예시
print(solution(["0123456789","9876543210","9999999999999"], 50000, 5, 5))