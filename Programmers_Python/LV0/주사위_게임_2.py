# https://school.programmers.co.kr/learn/courses/30/lessons/181930?language=python3

def solution(a, b, c):
    if (a == b) or (b == c) or (c == a):
        if (a == b) and (b == c):
            return (a+b+c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
        return (a+b+c) * (a**2 + b**2 + c**2)      
    return (a+b+c)
  
# 입출력 예시
print(solution(2, 6, 1))
print(solution(5, 3, 3))
print(solution(4, 4, 4))
