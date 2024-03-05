# https://school.programmers.co.kr/learn/courses/30/lessons/120853

def solution(s):
    s_lst = s.split()
    answer = 0
    tmp = 0

    for i in s_lst:
        if i == 'Z':
            answer -= tmp
        else:
            tmp = int(i)
            answer += tmp

    return answer

"""
list로 변환하는 과정에서 Z이전의 항목을 없애는 컴프리핸션 방식이 있으면 편할 것
"""

print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))
print(solution("-1 -2 -3 Z"))