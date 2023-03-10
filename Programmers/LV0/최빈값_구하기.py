# https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):
    dic_tmp = {}
    max_value, max_index = 0, 0
    duple_flg = False
    for n in array:
        if n not in dic_tmp:
            dic_tmp[n] = 0
        dic_tmp[n] += 1
        if dic_tmp[n] > max_value:
            max_value = dic_tmp[n]
            max_index = n
            duple_flg = False
        elif dic_tmp[n] == max_value:
            duple_flg = True
    return -1 if duple_flg else max_index

# 입출력 예시
print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))
