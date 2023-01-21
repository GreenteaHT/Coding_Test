# https://school.programmers.co.kr/learn/courses/30/lessons/136798

def solution(number, limit, power):
    answer = 0

    def div(num):
        cnt = 0
        n_half = num ** (1 / 2)
        for k in range(1, int(n_half) + 1):
            if num % k == 0:
                cnt += 2
        if n_half == int(n_half):
            cnt -= 1
        return cnt

    for i in range(1, number + 1):
        div_n = div(i)
        print(div_n)
        if div_n > limit:
            answer += power
        else:
            answer += div_n

    return answer


print(solution(5, 3, 2))
print(solution(10, 3, 2))
