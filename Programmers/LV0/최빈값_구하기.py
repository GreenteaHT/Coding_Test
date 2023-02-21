# https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):
    answer = 0
    dic_tmp = {}
    max_val = 0
    for i in array:
        if dic_tmp.get(i) is None:
            dic_tmp = 1
        else:
            dic_tmp[i] += 1

    return answer


dic = {}

if dic.get(1):
    print(1)
else:
    print(2)

