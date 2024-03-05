# https://school.programmers.co.kr/learn/courses/30/lessons/181909

def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[-i-1:])
    return sorted(answer)

# 입출력 예시
print(solution("banana"))
print(solution("programmers"))

