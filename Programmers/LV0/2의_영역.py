# https://school.programmers.co.kr/learn/courses/30/lessons/181894

def solution(arr):
    try:
        f_p = arr.index(2)
        l_p = arr[::-1].index(2)
        return arr[f_p:len(arr)-l_p]
    except:
        return [-1]

# 입출력 예시
print(solution([1, 2, 1, 4, 5, 2, 9]))
print(solution([1, 2, 1]))
print(solution([1, 1, 1]))
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))
print(solution([2]))