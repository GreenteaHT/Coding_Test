# https://school.programmers.co.kr/learn/courses/30/lessons/181871?language=python3

def solution(myString, pat):
    answer = 0
    for i in range(len(myString) - len(pat) + 1):
        # startswith 함수를 이용 가능
        if myString[i:i+len(pat)] == pat:
            answer += 1
    return answer

# 입출력 예시
print(solution("banana", "ana"))
print(solution("aaaa", "aa"))