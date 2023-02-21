# https://school.programmers.co.kr/learn/courses/30/lessons/120890

def solution(array, n):
    answer = 0
    tmp_min = 100
    for i in array:
        alu = abs(n-i)
        print(n, i, alu)
        if n <= i and alu < tmp_min:
            tmp_min = alu
            answer = i
        elif n >= i and alu <= tmp_min:
            tmp_min = alu
            answer = i
    return answer

# 입출력 예시
print(solution([3, 10, 28], 20))
print(solution([10, 11, 12], 13))