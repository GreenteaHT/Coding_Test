# https://school.programmers.co.kr/learn/courses/30/lessons/181880

def solution(num_list):
    answer = 0
    for n in num_list:
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                n -= 1
                n //= 2
            answer += 1
    return answer

# 입출력 예시
print(solution([12, 4, 15, 1, 14]))