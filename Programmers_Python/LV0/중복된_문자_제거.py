# https://school.programmers.co.kr/learn/courses/30/lessons/120888

def solution(my_string):
    asc_lst = [0]*128
    answer = ''
    for i in my_string:
        if asc_lst[ord(i)] == 0:
            answer += i
            asc_lst[ord(i)] = 1
    return answer

# 입출력 예시
print(solution("people"))
print(solution("We are the world"))
