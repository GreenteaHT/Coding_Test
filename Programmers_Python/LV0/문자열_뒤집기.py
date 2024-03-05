# https://school.programmers.co.kr/learn/courses/30/lessons/181905

def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
  
# 입출력 예시
print(solution("Progra21Sremm3", 6, 12))
print(solution("Stanley1yelnatS", 4, 10))
