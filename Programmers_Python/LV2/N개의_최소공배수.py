from functools import reduce

def solution(arr):
    # 최대공약수
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    # 최소공배수
    def lcm(a, b):
        return a * b // gcd(a, b)
    # reduce를 이용한 리스트의 최소공배수
    def lcm_multiple(numbers):
        return reduce(lcm, numbers)
    
    return lcm_multiple(arr)

print(solution([2, 6, 8, 14]))