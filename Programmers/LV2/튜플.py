# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    duple_check_set = set()
    answer = []
    s_lst = sorted([set(i.split(',')) for i in s[2:-2].split('},{')], key=lambda x: len(x))
    for i in s_lst:
        n = (i - duple_check_set).pop()
        answer.append(int(n))
        duple_check_set.add(n)
    return answer

# 입출력 예시
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
