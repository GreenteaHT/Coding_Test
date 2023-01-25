def solution(n):
    answer = 0
    b = 0
    while n != 0:
        n, b = divmod(n + b, 10)
        answer += n
        print(n)

    return answer


print(solution(100))
print(solution(1081))
# exception case
print(solution(1999))
