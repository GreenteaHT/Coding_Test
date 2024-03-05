# https://school.programmers.co.kr/learn/courses/30/lessons/181857#

def solution(arr):
    if len(arr) == 1:
        return arr
    binary_length = len(bin(len(arr)-1)) - 2
    arr += ([0] * (2**binary_length - len(arr)))
    return arr

    # 이진법 활용
    # def solution(arr):
    # l = len(arr)
    # while bin(l).count('1') != 1:
    #     l += l & (-l)
    # return arr + [0] * (l - len(arr))

# 입출력 예시
print(solution([1, 2, 3, 4, 5, 6]))
print(solution([58, 172, 746, 89]))