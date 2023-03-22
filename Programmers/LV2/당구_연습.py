# https://school.programmers.co.kr/learn/courses/30/lessons/169198?language=python3

def solution(m, n, startX, startY, balls):
    answer = []

    for i in balls:
        if startX == i[0]:
            answer.append(min(startX + i[0], (2 * m - startX - i[0])) ** 2 + (startY - i[1]) ** 2)
        elif startY == i[1]:
            answer.append((startX - i[0]) ** 2 + min(startY + i[1], (2 * n - startY - i[1])) ** 2)
        else:
            answer.append(min((startX - i[0]) ** 2 + min(startY + i[1], (2 * n - startY - i[1])) ** 2,
                              min(startX + i[0], (2 * m - startX - i[0])) ** 2 + (startY - i[1]) ** 2))
        # if startX + i[0] >= m:
        #     if startY + i[1] >= n:
        #         answer.append((2*m - startX - i[0])**2 + (2 * n - startY - i[1])**2)
        #     else:
        #         answer.append((2*m - startX - i[0])**2 + (startY + i[1])**2)
        # else:
        #     if startY + i[1] >= n:
        #         answer.append((startX + i[0]) ** 2 + (2 * n - startY - i[1]) ** 2)
        #     else:
        #         answer.append((startX + i[0]) ** 2 + (startY + i[1]) ** 2)
    return answer


print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))
