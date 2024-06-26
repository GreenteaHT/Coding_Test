# https://school.programmers.co.kr/learn/courses/30/lessons/134239

def solution(k, ranges):
    answer = []
    area = []
    graph = [k]
    
    while k > 1:
        if k%2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        area.append((graph[-1] + k)/2)
        graph.append(k)

    n = len(graph) - 1
    for range in ranges:
        a = range[0]
        b = range[1]
        if 0 <= a <= n and 0 <= -b <= n and a <= n + b:
            answer.append(sum(area[a : n + b]))
        else:
            answer.append(-1)
            
    return answer


# 테스트
print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))
print(solution(3, [[0,0], [1,-2], [3,-3]]))