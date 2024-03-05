# https://school.programmers.co.kr/learn/courses/30/lessons/181898

def solution(arr, idx):
    try:
        return arr.index(1, idx)
    except:
        return -1

# def solution(arr, idx):
#     for i in range(idx, len(arr)):
#         if arr[i] == 1:
#             return i
#     return -1

# 입출력 예시
print(solution([0, 0, 0, 1], 1))
print(solution([1, 0, 0, 1, 0, 0], 4))
print(solution([1, 1, 1, 1, 0], 3))