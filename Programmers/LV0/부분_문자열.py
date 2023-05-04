# https://school.programmers.co.kr/learn/courses/30/lessons/181842

def solution(str1, str2):
    return int(str1 in str2)

# 입출력 예시
print(solution("abc", "aabcc"))
print(solution("tbt", "tbbttb"))