# https://school.programmers.co.kr/learn/courses/30/lessons/388352

def generate_bit_combinations(n, k=5):  # Gosper's hack
    bitmask = (1 << k) - 1
    
    while bitmask < (1 << n):
        yield bitmask
        
        c = bitmask & -bitmask
        r = bitmask + c
        bitmask = (((r ^ bitmask) >> 2) // c) | r


def list_to_bitmask(numbers):
    bitmask = 0
    for num in numbers:
        bitmask |= (1 << (num - 1))
    return bitmask 


def solution(n, q, ans):
    possible_codes = list(generate_bit_combinations(n))
    
    for attempt, correct_count in zip(q, ans):
        attempt_mask = list_to_bitmask(attempt)
        possible_codes = [code for code in possible_codes if bin(code & attempt_mask).count('1') == correct_count]

    return len(possible_codes)

# 입출력 예시
print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))
print(solution(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1]))

# 다른 풀이
# 아뿔싸, set을 이용한 교집합 방법이 있었다!
# import itertools 

# def solution(n, q, ans):
#     f = list(itertools.combinations(range(1, n + 1), 5))

#     for g, cnt in zip(q, ans):
#          f = [code for code in f if len(set(code) & set(g)) == cnt]

#     return len(f)