# https://school.programmers.co.kr/learn/courses/30/lessons/181864

def solution(myString, pat):
    tmp_str = ''
    for i in myString:
        tmp_str += 'A' if i == 'B' else 'B'
    if pat in tmp_str:
        return 1
    else:
        return 0


print(solution("ABBAA", "AABB"))
print(solution("ABAB", "ABAB"))