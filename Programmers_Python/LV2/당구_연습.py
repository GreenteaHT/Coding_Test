# https://school.programmers.co.kr/learn/courses/30/lessons/169198?language=python3

def solution(m, n, startX, startY, balls):
    answer = []

    for i in balls:
        if startX == i[0]:
            answer.append(min(min(startX + i[0], (2 * m - startX - i[0])) ** 2 + (startY - i[1]) ** 2,
                          (2 * n - startY - i[1]) ** 2 if startY >= i[1] else (startY + i[1]) ** 2))
        elif startY == i[1]:
            answer.append(min((startX - i[0]) ** 2 + min(startY + i[1], (2 * n - startY - i[1])) ** 2,
                              (2 * m - startX - i[0]) ** 2 if startX >= i[0] else (startX + i[0]) ** 2))
        else:
            answer.append(min((startX - i[0]) ** 2 + min(startY + i[1], (2 * n - startY - i[1])) ** 2,
                              min(startX + i[0], (2 * m - startX - i[0])) ** 2 + (startY - i[1]) ** 2))
    return answer

# 입출력 예시
print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))
print(solution(10, 10, 5, 9, [[5, 8]]))
