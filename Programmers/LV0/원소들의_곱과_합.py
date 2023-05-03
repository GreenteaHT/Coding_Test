# https://school.programmers.co.kr/learn/courses/30/lessons/181929

def solution(num_list):
    num_sum = 0
    num_mul = 1
    for i in num_list:
        num_sum += i
        num_mul *= i
    return int(num_sum**2 > num_mul)

# 입출력 예시
print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))
