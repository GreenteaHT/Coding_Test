# https://school.programmers.co.kr/learn/courses/30/lessons/120924

def solution(common):
    if common[0] - common[1] == common[1] - common[2]:
        return common[-1] + common[1] - common[0]
    else:
        return common[-1] * common[1] // common[0]

# 입출력 예시
print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))