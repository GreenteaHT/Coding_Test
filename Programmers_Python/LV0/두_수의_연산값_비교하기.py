# https://school.programmers.co.kr/learn/courses/30/lessons/181938

def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)

# 입출력 예시
print(solution(2, 91))
print(solution(91, 2))
