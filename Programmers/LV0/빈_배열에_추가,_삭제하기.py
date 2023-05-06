# https://school.programmers.co.kr/learn/courses/30/lessons/181860

def solution(arr, flag):
    answer = []
    for i, j in zip(arr, flag):
        if j:
            answer.extend([i] * i * 2)
        else:
            for _ in range(i):
                answer.pop()
    return answer

# 입출력 예시
print(solution([3, 2, 4, 1, 3], [True, False, True, False, False]))