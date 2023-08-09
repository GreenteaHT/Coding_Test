# https://school.programmers.co.kr/learn/courses/30/lessons/181858

def solution(arr, k):
    set_k = set()   # 중복확인을 위한 set
    lst_k = []      # 순서 기억을 위한 list
    for i in arr:
        if i not in set_k:
            set_k.add(i)
            lst_k.append(i)
        if len(set_k) == k:
            return lst_k
    return lst_k + [-1] * (k - len(lst_k))

# 입출력 예시
print(solution([0, 1, 1, 2, 2, 3], 3))
print(solution([0, 1, 1, 1, 1], 4))