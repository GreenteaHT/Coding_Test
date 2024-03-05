# https://school.programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

def solution(participant, completion):
    par_dic = Counter(participant)
    com_dic = Counter(completion)

    for i in par_dic:
        if par_dic[i] != com_dic[i]:
            return i
    answer = ''
    return answer

# 입출력 예시
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))