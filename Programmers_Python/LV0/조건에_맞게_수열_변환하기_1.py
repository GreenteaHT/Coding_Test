# https://school.programmers.co.kr/learn/courses/30/lessons/181882

def solution(arr):
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i] % 2 == 0:
            arr[i] //= 2
        elif arr[i] < 50 and arr[i] % 2 == 1:
            arr[i] *= 2
    return arr

# 입출력 예시
print(solution([1, 2, 3, 100, 99, 98]))