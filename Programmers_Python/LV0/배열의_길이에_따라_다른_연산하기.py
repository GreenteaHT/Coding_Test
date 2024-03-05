# https://school.programmers.co.kr/learn/courses/30/lessons/181854

def solution(arr, n):
    len_arr = len(arr)
    if len_arr % 2 == 0:
        for i in range(1, len_arr + 1, 2):
            arr[i] += n
    else:
        for i in range(0, len_arr + 1, 2):
            arr[i] += n
    return arr

# 입출력 예시
print(solution([49, 12, 100, 276, 33], 27))
print(solution([444, 555, 666, 777], 100))
