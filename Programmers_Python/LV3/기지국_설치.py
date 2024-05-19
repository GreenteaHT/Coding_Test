# https://school.programmers.co.kr/learn/courses/30/lessons/12979

def solution(n, stations, w):
    need_AP = 0
    # 한 ap node가 커버할 수 있는 거리
    coverage_distance = w*2 + 1
    
    # 각 원래있는 노드들 사이의 커버가 되지 않는 거리를 계산
    # 커버가 되면 need_AP에는 0이 더해질 것
    last_node = -w
    for position in stations:
        need_AP += (position - last_node - 1) // coverage_distance
        last_node = position
    # 마지막 노드부터 끝까지의 필요 ap node 개수 추가
    return need_AP + (n - last_node + w)//coverage_distance

# 입출력 예시
print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))