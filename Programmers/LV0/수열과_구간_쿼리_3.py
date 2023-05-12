# https://school.programmers.co.kr/learn/courses/30/lessons/181924

def solution(arr, queries):
    for i in queries:
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]
    return arr

# 입출력 예시
print(solution([0, 1, 2, 3, 4], [[0, 3],[1, 2],[1, 4]]))
