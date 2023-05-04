# https://school.programmers.co.kr/learn/courses/30/lessons/181873

def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())

# 입출력 예시
print(solution("programmers", "p"))
print(solution("lowercase", "x"))