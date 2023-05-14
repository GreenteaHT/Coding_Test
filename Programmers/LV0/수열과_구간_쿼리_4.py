# https://school.programmers.co.kr/learn/courses/30/lessons/181922

def solution(arr, queries):
    for q in queries:
        for i in range((q[0] + q[2] - 1) // q[2] * q[2], q[1] + 1, q[2]):
            arr[i] += 1
	return arr

# 입출력 예시
print(solution([0, 1, 2, 4, 3], [[0, 4, 1],[0, 3, 2],[0, 3, 3]]))
