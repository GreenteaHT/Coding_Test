# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    p_len = len(p)
    for i in range(len(t) - p_len + 1):
        if int(t[i:i+p_len]) <= int(p):
            answer += 1
    return answer

# 입출력 예시
print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))