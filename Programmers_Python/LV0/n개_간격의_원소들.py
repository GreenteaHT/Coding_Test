# https://school.programmers.co.kr/learn/courses/30/lessons/181888

def solution(num_list, n):
    return num_list[::n]

# 입출력 예시
print(solution([4, 2, 6, 1, 7, 6], 2))
print(solution([4, 2, 6, 1, 7, 6], 4))