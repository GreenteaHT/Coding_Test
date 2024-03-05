# https://school.programmers.co.kr/learn/courses/30/lessons/181881

def solution(arr):
    tmp = [0] * len(arr)
    cnt = 0
    while arr != tmp:
        tmp = arr.copy()
        cnt += 1
        for n, i in enumerate(arr):
            if i % 2 == 0 and i >= 50:
                arr[n] = i // 2
            elif i % 2 == 1 and i < 50:
                arr[n] = i * 2 + 1
            else:
                arr[n] = i
    return cnt - 1

# 입출력 예시
print(solution([1, 2, 3, 100, 99, 98]))