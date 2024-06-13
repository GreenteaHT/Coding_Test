# https://school.programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    # 행렬 생성
    matrix = [[i + j * columns for i in range(1, columns+1)] for j in range(0, rows)]
    min_list = []
    
    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        border_elements = []
        
        ## 회전시킬 데이터 저장
        # 윗변
        for y in range(y1, y2 + 1):
            border_elements.append(matrix[x1][y])
        # 오른쪽 변
        for x in range(x1 + 1, x2 + 1):
            border_elements.append(matrix[x][y2])
        # 아랫변
        for y in range(y2 - 1, y1 - 1, -1):
            border_elements.append(matrix[x2][y])
        # 왼쪽 변
        for x in range(x2 - 1, x1, -1):
            border_elements.append(matrix[x][y1])
        
        # 최소값 추출
        min_list.append(min(border_elements))
        # 회전  
        border_elements = [border_elements[-1]] + border_elements[:-1]
        
        # 회전 후 행렬에 적용
        index = 0
        # 윗변
        for y in range(y1, y2 + 1):
            matrix[x1][y] = border_elements[index]
            index += 1
        # 오른쪽 변
        for x in range(x1 + 1, x2 + 1):
            matrix[x][y2] = border_elements[index]
            index += 1
        # 아랫변
        for y in range(y2 - 1, y1 - 1, -1):
            matrix[x2][y] = border_elements[index]
            index += 1
        # 왼쪽 변
        for x in range(x2 - 1, x1, -1):
            matrix[x][y1] = border_elements[index]
            index += 1
        
    return min_list

# 테스트
print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))
