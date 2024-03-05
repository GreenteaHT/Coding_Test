# https://school.programmers.co.kr/learn/courses/30/lessons/181917

def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)
  
# 입출력 예시
print(solution(False, True, True, True))
print(solution(True, False, False, False))
