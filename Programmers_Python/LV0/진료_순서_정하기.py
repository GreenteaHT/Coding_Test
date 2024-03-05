# https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    emergency_dict = {string: len(emergency) - i for i, string in enumerate(emergency)}
    emergency_dict_sorted = dict(sorted(emergency_dict.items()))
    print(emergency_dict_sorted)
    return list(emergency_dict_sorted.values())

# 입출력 예시
print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([30, 10, 23, 6, 100]))