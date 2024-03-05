# https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people.sort(reverse=True)
    heavy_index, light_index = 0, len(people) - 1
    cnt = 0

    while heavy_index <= light_index:
        if people[heavy_index] + people[light_index] <= limit:
            light_index -= 1
        heavy_index += 1
        cnt += 1
    return cnt

# 입출력 예시
print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))

## remove를 이용하여 시간복잡도가 큼
# import sys
# sys.setrecursionlimit(50000)
#
# def solution(people, limit):
#     people.sort(reverse=True)
#
#     cnt = 0
#     while people:
#         weight_limit = limit
#         rest_people = []
#         max_people = 2
#         for n, p in enumerate(people):
#             # print(n, p, rest_people, people)
#             if max_people == 0:
#                 break
#             if p < weight_limit:
#                 weight_limit -= p
#                 rest_people.append(n)
#                 max_people -= 1
#             elif weight_limit == p:
#                 weight_limit -= p
#                 rest_people.append(n)
#                 max_people -= 1
#                 break
#         for r in reversed(rest_people):
#             del people[r]
#         cnt += 1
#     return cnt
