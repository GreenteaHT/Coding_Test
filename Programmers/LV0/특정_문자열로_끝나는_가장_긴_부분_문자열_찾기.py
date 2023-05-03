# https://school.programmers.co.kr/learn/courses/30/lessons/181872

def solution(myString, pat):
    return myString[:myString.rindex(pat) + len(pat)]

# 입출력 예시
print(solution("AbCdEFG", "dE"))
print(solution("AAAAaaaa", "a"))