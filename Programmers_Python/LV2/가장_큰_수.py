# https://school.programmers.co.kr/learn/courses/30/lessons/42746

from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    result = ''.join(numbers)
    
    return result

# 테스트
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))