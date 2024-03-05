# https://school.programmers.co.kr/learn/courses/30/lessons/181843

def solution(my_string, target):
    return int(target in my_string)

# 입출력 예시
print(solution("banana", "ana"))
print(solution("banana", "wxyz"))