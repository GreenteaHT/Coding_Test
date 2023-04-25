# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort()
    max_h = 0

    for h in range(1, len(citations) + 1):
        if citations.pop() >= h:
            max_h = h
        else:
            break
    return max_h

# 입출력 예시
print(solution([3, 0, 6, 1, 5]))
print(solution([0]))
print(solution([1]))
print(solution([1000]))
