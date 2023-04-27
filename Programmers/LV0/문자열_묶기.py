# https://school.programmers.co.kr/learn/courses/30/lessons/181855

def solution(strArr):
    cnt_dic = {}
    for i in strArr:
        length = len(i)
        if length in cnt_dic:
            cnt_dic[length] += 1
        else:
            cnt_dic[length] = 1
    return max(cnt_dic.values())

# 입출력 예시
print(solution(["a","bc","d","efg","hi"]))