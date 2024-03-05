# https://school.programmers.co.kr/learn/courses/30/lessons/181830

def solution(arr):
    Height = len(arr)
    Width = len(arr[0])
    if Height > Width:
        for i in range(Height):
            arr[i] += [0]*(Height-Width)
    elif Height < Width:
        arr += [[0]*Width for _ in range(Width-Height)]
    return arr

# 입출력 예시
print(solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]))
print(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))
print(solution([[1, 2], [3, 4]]))