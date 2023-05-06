# https://school.programmers.co.kr/learn/courses/30/lessons/181866

import re

def solution(myString):
    return sorted(re.split(r'[x]+', myString.strip('x')))

# 입출력 예시
print(solution("axbxcxdx"))
print(solution("dxccxbbbxaaaa"))