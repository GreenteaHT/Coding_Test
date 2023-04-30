# https://school.programmers.co.kr/learn/courses/30/lessons/181849

def solution(num_str):
    answer = 0
    for i in num_str:
        answer += int(i)
    return answer

# 입출력 예시
print(solution("123456789"))
print(solution("1000000"))