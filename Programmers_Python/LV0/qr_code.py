# https://school.programmers.co.kr/learn/courses/30/lessons/181903
# 관련 문제
# - 세로 읽기
# - https://school.programmers.co.kr/learn/courses/30/lessons/181904

def solution(q, r, code):
    return code[r::q]

print(solution(3, 1, "qjnwezgrpirldywt"))
print(solution(1, 0, "programmers"))