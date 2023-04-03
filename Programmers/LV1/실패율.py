# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    stg_lst = [0] * (N + 2)
    failure_dic = {key: 0 for key in range(1, N + 1)}
    for i in stages:
        stg_lst[i] += 1

    for j in range(1, N + 1):
        failure_dic[j] = stg_lst[j] / sum(stg_lst[j:])
        if failure_dic[j] == 1:
            break

    answer = sorted(failure_dic, key=lambda x: failure_dic[x], reverse=True)
    return answer

# 입출력 예시
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
