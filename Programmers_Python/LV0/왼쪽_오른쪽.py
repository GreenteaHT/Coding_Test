# https://school.programmers.co.kr/learn/courses/30/lessons/181890

def solution(str_list):
    for n in range(len(str_list)):
        if str_list[n] == 'l':
            return str_list[:n]
        elif str_list[n] == 'r':
            return str_list[n+1:]
    return []

# 입출력 예시
print(solution(["u", "u", "l", "r"]))
print(solution(["l"]))