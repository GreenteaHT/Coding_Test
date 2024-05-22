# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

# 소수 체크
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # 6n +-1 법칙 활용
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solution(numbers):
    primes = set()
    
    # 몇개의 숫자를 고를 건지
    for length in range(1, len(numbers) + 1):
        # 고른 숫자의 조합
        for perm in permutations(numbers, length):
            num = int(''.join(perm))
            if is_prime(num):
                primes.add(num)
    
    return len(primes)

# 입출력 예시
print(solution("17"))
print(solution("011"))