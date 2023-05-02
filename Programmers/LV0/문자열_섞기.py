# https://school.programmers.co.kr/learn/courses/30/lessons/181942

def solution(str1, str2):
    answer = ''
    for a, b in zip(str1, str2):
        answer += a + b
    return answer
  
# 입출력 예시
print(solution("aaaaa", "bbbbb"))
