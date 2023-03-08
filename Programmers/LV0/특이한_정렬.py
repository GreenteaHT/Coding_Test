# https://school.programmers.co.kr/learn/courses/30/lessons/120880

def solution(numlist, n):
    numlist_sub = list(map(lambda x: abs(x - n - 0.1), numlist))
    numlist_dict = {string: numlist[i] for i, string in enumerate(numlist_sub)}
    numlist_dict_sorted = dict(sorted(numlist_dict.items()))
    return list(numlist_dict_sorted.values())

# def solution(numlist, n):
#     return sorted(numlist, key=lambda x: (abs(x - n), n - x))

# 입출력 예시
print(solution([1, 2, 3, 4, 5, 6], 4))
print(solution([10000,20,36,47,40,6,10,7000], 30))