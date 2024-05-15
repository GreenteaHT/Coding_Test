# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    # k진수로 변환
    def convert_to_base_k(n, k):
        result = ''
        while n > 0:
            result = str(n % k) + result
            n //= k
        return result
    
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
    
    # k 진수 변환 후 0을 기준으로 분리
    candidates = convert_to_base_k(n, k).split('0')

    cnt = 0
    for candidate in candidates:
        if candidate and is_prime(int(candidate)):
            cnt += 1
    
    return cnt

# 입출력 예시
print(solution(437674, 3))
print(solution(110011, 10))