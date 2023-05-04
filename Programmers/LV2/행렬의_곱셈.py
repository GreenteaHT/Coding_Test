# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    return [[sum(a * b for a, b in zip(i, j)) for i in zip(*arr2)] for j in arr1]

# 입출력 예시
print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))