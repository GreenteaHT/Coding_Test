# https://school.programmers.co.kr/learn/courses/30/lessons/12900

# 이를 요구하지 않음
def nCk(n, k):
    numerator, denominator = 1, 1
    k = min(n-k, k)
    for i in range(1, k+1):
        denominator *= i
        numerator *= n - i + 1
    return numerator//denominator

# 피보나치 수열을 이용하는 함정 문제
def solution(n):
    p1 = 0
    p2 = 1
    for i in range(n):
        tmp = p1 + p2
        p1 = p2
        p2 = tmp
    return p2 % 1000000007

    # answer = 0
    # for i in range(n//2 + 1):
    #     answer += nCk(n-i, i)
    #     if answer >= 1000000007:
    #         answer %= 1000000007
    # return answer

# 입출력 예시
for i in range(1, 10):
    print(solution(i))