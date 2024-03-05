# https://school.programmers.co.kr/learn/courses/30/lessons/181865

def solution(binomial):
    return eval(binomial)
    # a, op, b = binomial.split(' ')
    # a, b = int(a), int(b)
    # if op == '+':
    #     return a + b
    # elif op == '-':
    #     return a - b
    # elif op == '*':
    #     return a * b

# 입출력 예시
print(solution("43 + 12"))
print(solution("0 - 7777"))
print(solution("40000 * 40000"))