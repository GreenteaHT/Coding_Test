# https://school.programmers.co.kr/learn/courses/30/lessons/147354

from functools import reduce

def solution(data, col, row_begin, row_end):
    # 기준에 따라 정렬
    data = sorted(data, key= lambda x : (x[col - 1], -x[0]))
    
    hesh = [0] * (row_end - row_begin + 1)
    for i in range(row_begin, row_end+1):
        hesh[row_begin - i] += sum([val%i for val in data[i - 1]])
    
    return reduce(lambda x, y: x ^ y, hesh)  # XOR

# 테스트
print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3))