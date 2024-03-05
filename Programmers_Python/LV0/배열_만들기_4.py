# https://school.programmers.co.kr/learn/courses/30/lessons/181918

def solution(arr):
    stk = []
    i = 0  
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif stk[-1] >= arr[i]:
            stk.pop()
    return stk

# 입출력 예시
print(solution([1, 4, 2, 5, 3]))
