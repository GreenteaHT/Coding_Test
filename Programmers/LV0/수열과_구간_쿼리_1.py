# https://school.programmers.co.kr/learn/courses/30/lessons/181883

def solution(arr, queries):
    for i in queries:
        for j in range(i[0], i[1]+1):
            arr[j] += 1
    return arr
  
# 입출력 예시
print(solution([0, 1, 2, 3, 4], [[0, 1],[1, 2],[2, 3]]))
