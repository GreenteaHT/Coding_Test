# https://school.programmers.co.kr/learn/courses/30/lessons/181935

def solution(n):
    if n % 2 == 0:
        a = n // 2
        # 등차 수열 제곱 합 공식 이용
        return a*(a + 1)*(2*a + 1) // 3 * 2
    else:
        # 등차 수열 합 공식 이용
        a = (n + 1) // 2
        return a ** 2
      
# 입출력 예시
print(solution(7))
print(solution(10))
