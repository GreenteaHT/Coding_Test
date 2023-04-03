# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    # lost = sorted(lost)
    # reserve = sorted(reserve)
    cnt = 0
    for i in lost:
        if (i - 1) in reserve:
            reserve.remove(i - 1)
            cnt += 1
        elif (i + 1) in reserve:
            reserve.remove(i + 1)
            cnt += 1
    answer = n - len(lost) + cnt

    return answer

# 입출력 예시
print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))