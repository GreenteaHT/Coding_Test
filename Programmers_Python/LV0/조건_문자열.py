# https://school.programmers.co.kr/learn/courses/30/lessons/181934

def solution(ineq, eq, n, m):
    return int(eval("%d %s%s %d" %(n, ineq, eq, m)) if eq == "=" else eval("%d %s %d" %(n, ineq, m)))

# 입출력 예시
print(solution("<", "=", 20, 50))
print(solution(">", "!", 41, 78))