# https://school.programmers.co.kr/learn/courses/30/lessons/181861

def solution(arr):
    answer = []
    for i in arr:
        answer += [i] * i
    return answer

# 입출력 예시
print(solution([5, 1, 4]))
print(solution([6, 6]))
print(solution([1]))

# 이중 컴프리헨션
# def solution(arr):
# return [i for i in arr for j in range(i)]
