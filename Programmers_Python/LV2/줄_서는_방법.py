# https://school.programmers.co.kr/learn/courses/30/lessons/12936

import math

def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))
    max_len = math.factorial(n)
    k -= 1  # 0기준 인덱스로 바꿈
    
    while n > 0:
        max_len //= n
        n -= 1
        index, k = divmod(k, max_len)
        # 사용한 숫자는 결과에 넣고 기존 리스트에서 제거
        answer.append(numbers.pop(index))

    return answer

# 테스트
print(solution(3, 5))