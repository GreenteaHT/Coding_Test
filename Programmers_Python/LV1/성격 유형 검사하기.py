# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    per_lst = ["R", "T", "C", "F", "J", "M", "A", "N"]
    per_dic = {ind: 0 for ind in per_lst}
    for i in range(len(survey)):
        ind1, ind2 = survey[i][0], survey[i][1]
        scr = choices[i] - 4
        if scr < 0:
            per_dic[ind1] += abs(scr)
        elif scr > 0:
            per_dic[ind2] += scr
    personality = ""
    for j in range(4):
        ind1, ind2 = per_lst[j*2], per_lst[j*2+1]
        personality += ind1 if per_dic[ind1] >= per_dic[ind2] else ind2
    return personality

# 입출력 예시
print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], 	[7, 1, 3]))

## OrderedDict 풀이
# from collections import OrderedDict
#
# def solution(survey, choices):
#     per_dic = OrderedDict({'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0})
#     for i in range(len(survey)):
#         ind1, ind2 = survey[i][0], survey[i][1]
#         scr = choices[i] - 4
#         if scr < 0:
#             per_dic[ind1] += abs(scr)
#         elif scr > 0:
#             per_dic[ind2] += scr
#     personality = ""
#
#     per_lst = list(per_dic.items())
#     for j in range(4):
#         ind1, val1 = per_lst[j * 2]
#         ind2, val2 = per_lst[j * 2 + 1]
#         personality += ind1 if val1 >= val2 else ind2
#     return personality
