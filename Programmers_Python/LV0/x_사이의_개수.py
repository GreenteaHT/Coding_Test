# https://school.programmers.co.kr/learn/courses/30/lessons/181867

def solution(myString):
    return [len(i) for i in myString.split('x')]

# 입출력 예시
print(solution("oxooxoxxox"))
print(solution("xabcxdefxghi"))