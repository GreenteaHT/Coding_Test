# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    answer = 0
    while storey != 0:
        n10 = storey % 10
        if (storey // 10) % 10 >= 5:
            if n10 >= 5:
                answer += 10 - n10
                storey += 10 - n10
            else:
                answer += n10
        else:
            if n10 >= 6:
                answer += 10 - n10
                storey += 10 - n10
            else:
                answer += n10
        storey //= 10

    return answer

# 입출력 예시
print(solution(19999))
print(solution(16))
print(solution(2554))
