# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    ty, tm, td = map(int, today.split('.'))
    terms_dic = {}
    answer = []
    for i in terms:
        tmp = i.split(' ')
        terms_dic[tmp[0]] = int(tmp[1])
    for n, j in enumerate(privacies):
        day, terms_prv = j.split(' ')
        py, pm, pd = map(int, day.split('.'))
        due = 336 * (ty - py) + 28 * (tm - pm) + (td - pd)
        if due >= terms_dic[terms_prv] * 28:
            answer.append(n + 1)
    return answer

# 입출력 예시
print(
    (solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])))
print((solution("2020.01.01", ["Z 3", "D 5"],
                ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])))
