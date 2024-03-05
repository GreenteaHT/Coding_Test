# https://school.programmers.co.kr/learn/courses/30/lessons/120808

from math import gcd

def solution(numer1, denom1, numer2, denom2):
    numer1, denom1 = irr_frac(numer1, denom1)
    numer2, denom2 = irr_frac(numer2, denom2)
    denom_gcd = gcd(denom1, denom2)
    numer1 *= denom2 // denom_gcd
    numer2 *= denom1 // denom_gcd
    numer3 = numer1 + numer2
    denom3 = denom1 * denom2 // denom_gcd
    numer3, denom3 = irr_frac(numer3, denom3)
    return [numer3, denom3]

def irr_frac(n1, n2):
    g = gcd(n1, n2)
    if g != 1:
        n1 //= g
        n2 //= g
    return n1, n2

# 입출력 예시
print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))