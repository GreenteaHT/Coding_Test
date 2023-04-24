# https://school.programmers.co.kr/learn/courses/30/lessons/181893

def solution(arr, query):
    # 매번 슬라이싱 시에 시간복잡도 증가 -> 포인터 지정 계산
    arr_front_pointer = 0
    arr_rear_pointer = len(arr)
    for i, q in enumerate(query):
        if i % 2 == 0:
            arr_rear_pointer = arr_front_pointer + q + 1
        elif i % 2 == 1:
            arr_front_pointer += q
        # print(arr_front_pointer, arr_rear_pointer)
    return arr[arr_front_pointer:arr_rear_pointer]

# 입출력 예시
print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]))
