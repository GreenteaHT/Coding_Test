# https://school.programmers.co.kr/learn/courses/30/lessons/120842

def solution(num_list, n):
    answer_lst = [[0] * n for _ in range(len(num_list)//n)]
    for nth, i in enumerate(num_list):
        answer_lst[nth // n][nth % n] = i
    return answer_lst

# 입출력 예시
print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))
