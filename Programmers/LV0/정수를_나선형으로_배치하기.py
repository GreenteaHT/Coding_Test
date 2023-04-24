# https://school.programmers.co.kr/learn/courses/30/lessons/181832

def solution(n):
    lst1 = [[0]*n for _ in range(n)]
    a = n
    # 전 과정의 순서
    tmp = 1

    while a > n-a:
        pnt = n - a
        for i in range(pnt, a-1):
            lst1[pnt][i] = i + tmp - pnt
            lst1[i][a-1] = i + (a-1 - pnt) + tmp - pnt
            lst1[a-1][-(i+1)] = i + 2*(a-1 - pnt) + tmp - pnt
            lst1[-(i+1)][pnt] = i + 3*(a-1 - pnt) + tmp - pnt
        # 루프 문 안에서 += 4를 대입해도 좋다.
        tmp += (a - 1 - pnt) * 4
        a -= 1
    if n % 2 == 1:
        lst1[n//2][n//2] = tmp

    return lst1

# 입출력 예시
print(solution(4))
print(solution(5))



## GPT 생성 알고리즘, 포인터 사용
# def spiral_matrix(n):
#     matrix = [[0 for x in range(n)] for y in range(n)]
#     left, top, right, bottom = 0, 0, n - 1, n - 1
#     num = 1
#
#     while left <= right and top <= bottom:
#         # Move right
#         for i in range(left, right + 1):
#             matrix[top][i] = num
#             num += 1
#         top += 1
#
#         # Move down
#         for i in range(top, bottom + 1):
#             matrix[i][right] = num
#             num += 1
#         right -= 1
#
#         # Move left
#         if top <= bottom:
#             for i in range(right, left - 1, -1):
#                 matrix[bottom][i] = num
#                 num += 1
#             bottom -= 1
