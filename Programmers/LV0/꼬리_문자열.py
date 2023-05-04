# https://school.programmers.co.kr/learn/courses/30/lessons/181841

def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex not in i:
            answer += i
    return answer

# 입출력 예시
print(solution(["abc", "def", "ghi"], "ef"))
print(solution(["abc", "bbc", "cbc"], 'c'))