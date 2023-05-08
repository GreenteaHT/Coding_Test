# https://school.programmers.co.kr/learn/courses/30/lessons/181868

import re

def solution(my_string):
    return re.split(r'[ ]+', my_string.strip(' '))

# 입출력 예시
print(solution("i  love you"))
print(solution("    programmers  "))