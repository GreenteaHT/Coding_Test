# https://school.programmers.co.kr/learn/courses/30/lessons/181923

def solution(arr, queries):
    answer = []
    for i in queries:
        tmp = 1000001
        for j in range(i[0], i[1]+1):
            if arr[j] > i[2]:
                tmp = min(tmp, arr[j])
        answer.append(-1 if tmp == 1000001 else tmp)
    return answer

# 입출력 예시
print(solution([0, 1, 2, 4, 3], [[0, 4, 2],[0, 3, 2],[0, 2, 2]]))
