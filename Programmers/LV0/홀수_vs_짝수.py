# https://school.programmers.co.kr/learn/courses/30/lessons/181887

def solution(num_list):
    return max(sum(num_list[0::2]), sum(num_list[1::2]))

# 입출력 예시
print(solution([4, 2, 6, 1, 7, 6]))
print(solution([-1, 2, 5, 6, 3]))