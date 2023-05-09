# https://school.programmers.co.kr/learn/courses/30/lessons/181895

def solution(arr, intervals):
    answer = []
    for i in intervals:
        answer += arr[i[0]: i[1]+1]
    return answer

# 입출력 예시
print(solution([1, 2, 3, 4, 5], [[1, 3], [0, 4]]))