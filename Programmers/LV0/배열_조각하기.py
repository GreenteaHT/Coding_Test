# https://school.programmers.co.kr/learn/courses/30/lessons/181893

def solution(arr, query):
    arr_front_pointer = 0
    arr_rear_pointer = len(arr)
    for q in query:
        if q % 2 == 0 and arr_rear_pointer >= q:
            arr_rear_pointer -= q
        elif q % 2 == 1 and arr_front_pointer <= q:
            arr_front_pointer += q
    return arr[arr_front_pointer:arr_rear_pointer]

# 입출력 예시
print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]))
