# https://school.programmers.co.kr/learn/courses/30/lessons/62048

import math

# def solution(w, h):
#     w, h = min(w, h), max(w, h)
#     gcd = math.gcd(w, h)
#
#     n_blank_box = 0
#     y = 0
#     for i in range(1, h//gcd + 1):
#         if (w*i)//h == y:
#             n_blank_box += 1
#         else:
#             n_blank_box += 2
#             y += 1
#     n_blank_box = (n_blank_box - 1) * gcd
#     return w * h - n_blank_box

def solution(w, h):
    w, h = min(w, h), max(w, h)
    gcd = math.gcd(w, h)
    return w * h - (h//gcd + (w//gcd - 1)) * gcd

# 입출력 예시
print(solution(8, 12))


