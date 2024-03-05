# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    strat_row, start_point = divmod(left, n)
    end_row, end_point = divmod(right, n)
    height = end_row - strat_row + 1
    length = right - left + 1

    n_lst = [0] * length

    # 슬라이싱 하지 않는 방법으로 만들어야함
    # 패턴이 있기에 max를 쓰지 않아도 될듯


    # n_lst = [0] * (height * n)
    # for i in range(height):
    #     for j in range(n):
    #         n_lst[n * i + j] = max(strat_row + i + 1, j + 1)

    return n_lst[start_point:height*(n-1)+end_point+1]




# 입출력 예시
print(solution(3, 2, 5))
print(solution(4, 7, 14))


123
223
333