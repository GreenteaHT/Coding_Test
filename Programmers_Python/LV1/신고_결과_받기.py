# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    id_rep_dic = {key: set() for key in id_list}
    id_res_dic = {key: 0 for key in id_list}

    for rep_case in report:
        A, B = rep_case.split(' ')
        id_rep_dic[B].add(A)

    for value in id_rep_dic.values():
        if len(value) >= k:
            for reporter in value:
                id_res_dic[reporter] += 1

    answer = []
    for user in id_list:
        answer.append(id_res_dic[user])
    return answer

# 입출력 예시
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
