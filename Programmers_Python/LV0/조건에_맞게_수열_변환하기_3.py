# https://school.programmers.co.kr/learn/courses/30/lessons/181835?language=python3

def solution(arr, k):
    if k % 2 == 0:
        return [i+k for i in arr]
    else:
        return [i*k for i in arr]

# 입출력 예시
print(solution([1, 2, 3, 100, 99, 98], 3))
print(solution([1, 2, 3, 100, 99, 98], 2))