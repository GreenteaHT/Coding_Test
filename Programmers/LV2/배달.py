# https://school.programmers.co.kr/learn/courses/30/lessons/12978

def solution(N, road, K):
    # BFS, 다익스트라, 플루이드 등 경로 알고리즘 찾아보기
    road_dic = {i[0]: i[1:] for i in road}
    for i in road:
        road_dic[i[1]] += [i[0], i[2]]

    answer= 0
    return answer

# 입출력 예시
print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))