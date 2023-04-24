# https://school.programmers.co.kr/learn/courses/30/lessons/181916

def solution(a, b, c, d):
    num = [a, b, c, d]
    n_lst = [num.count(i) for i in num]
    score = 0

    print(num[n_lst.index(4)])

    # if max(n_lst) == 4:
    #     score += 1111 * n_lst.index(3)
    # elif max(n_lst) == 3:
    #     score += (10 * n_lst.index(3) + n_lst.index(1))**2
    # elif max(n_lst) == 2 and 1 not in n_lst:




    return score

# 입출력 예시
print(solution(2, 2, 2, 2))
print(solution(4, 1, 4, 4))
print(solution(6, 3, 3, 6))
print(solution(2, 5, 2, 6))
print(solution(6, 4, 2, 5))