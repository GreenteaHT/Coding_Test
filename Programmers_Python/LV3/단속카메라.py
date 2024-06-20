# https://school.programmers.co.kr/learn/courses/30/lessons/42884

from collections import deque

def solution(routes):
    camera = 0
    routes = deque(sorted(routes))
    while routes:
        ent, ext = routes.popleft()
        while routes and ext >= routes[0][0]:
            ext = min(ext, routes.popleft()[1])
        camera += 1
    return camera

# 테스트
print(solution([-20,-15], [-14,-5], [-18,-13], [-5,-3]))  # 2


## 훨씬 간단하게 차량의 전출 지점을 기준으로 오름차순 체크를 함
# def solution(routes):
#     routes = sorted(routes, key=lambda x: x[1])
#     last_camera = -30000

#     answer = 0

#     for route in routes:
#         if last_camera < route[0]:
#             answer += 1
#             last_camera = route[1]

#     return answer