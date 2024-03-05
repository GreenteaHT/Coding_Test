# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    tang_dic = {}
    # 딕셔너리에 귤 크기에 따른 개수 저장
    for i in tangerine:
        if i in tang_dic:
            tang_dic[i] += 1
        else:
            tang_dic[i] = 1

    # 딕셔너리의 value 값만 가져와 역순으로 더함
    cnt = 0
    for n, j in enumerate(sorted(tang_dic.values(), reverse=True)):
        cnt += j
        if cnt >= k:
            return n + 1
    return 1

# 입출력 예시
print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))