# https://school.programmers.co.kr/learn/courses/30/lessons/181840

def solution(num_list, n):
    if n in num_list:
        return 1
    else:
        return 0

# 입출력 예시
print(solution([1, 2, 3, 4, 5], 3))
print(solution([15, 98, 23, 2, 15], 20))