# https://school.programmers.co.kr/learn/courses/30/lessons/181904

def solution(my_string, m, c):
    answer = ''
    for i in range(0, len(my_string), m):
        answer += my_string[i:i+m][c-1]
    return answer

# 입출력 예시
print(solution("ihrhbakrfpndopljhygc", 4, 2))
print(solution("programmers", 1, 1))

# 슬라이싱 이용
# def solution(s, m, c):
#     return s[c-1::m]