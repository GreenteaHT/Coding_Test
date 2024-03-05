# https://school.programmers.co.kr/learn/courses/30/lessons/181916

def solution(a, b, c, d):
    num = [a, b, c, d]
    n_count = [num.count(i) for i in num]
    
    if max(n_count) == 4:
        return 1111 * a
    elif max(n_count) == 3:
        return (10 * num[n_count.index(3)] + num[n_count.index(1)])**2
    elif max(n_count) == 2:
        if min(n_count) == 2:
            return (a + c) *  abs(a - c) if a == b else (a + b) * abs(a - b)
        else:
            return (a * b * c * d) / num[n_count.index(2)]**2
    else:
        return min(num)

# 입출력 예시
print(solution(2, 2, 2, 2))
print(solution(4, 1, 4, 4))
print(solution(6, 3, 3, 6))
print(solution(2, 5, 2, 6))
print(solution(6, 4, 2, 5))