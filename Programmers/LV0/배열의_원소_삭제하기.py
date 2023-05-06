# https://school.programmers.co.kr/learn/courses/30/lessons/181844

def solution(arr, delete_list):
    delete_set = set(delete_list)
    return [i for i in arr if i not in delete_set]

# 입출력 예시
print(solution([293, 1000, 395, 678, 94], [94, 777, 104, 1000, 1, 12]))
print(solution([110, 66, 439, 785, 1], [377, 823, 119, 43]))