# https://school.programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    # 전행의 값 중 높은 값을 각 열에 누적시킴
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][k] for k in range(4) if k != j)
    
    return max(land[len(land) - 1])


# 테스트 예시
print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))  # 16