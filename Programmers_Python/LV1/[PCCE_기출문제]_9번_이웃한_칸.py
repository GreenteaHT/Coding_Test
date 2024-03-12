# https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board, h, w):
    # 1
    n = len(board[0])
    # 2
    count = 0
    # 3
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    # 4
    for i in range(4):
        # 4-1
        h_check = h + dh[i]
        w_check = w + dw[i]
        # 4-2
        if h_check >= 0 and h_check < n and w_check >= 0 and w_check < n:
            # 4-2-a
            if board[h][w] == board[h_check][w_check]:
                count += 1
    
    return count

# 입출력 예시
print(solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], 1, 1))
