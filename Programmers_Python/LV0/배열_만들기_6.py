# https://school.programmers.co.kr/learn/courses/30/lessons/181859

def solution(arr):
    stk = []
    for i in arr:
        if stk == []:
            stk.append(i)
        elif stk[-1] == i:
            stk.pop()
        elif stk[-1] != i:
            stk.append(i)
    if stk == []:
        return [-1]
    else:
        return stk
    
# 입출력 예시
print(solution([0, 1, 1, 1, 0]))
print(solution([0, 1, 0, 1, 0]))
print(solution([0, 1, 1, 0]))