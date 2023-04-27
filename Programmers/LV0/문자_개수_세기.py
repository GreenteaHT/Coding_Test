# https://school.programmers.co.kr/learn/courses/30/lessons/181902

def solution(my_string):
    alp_dic = {}
    for i in range(65, 91):
        alp_dic[chr(i)] = 0
    for i in range(97, 123):
        alp_dic[chr(i)] = 0

    for c in my_string:
        alp_dic[c] += 1
    return list(alp_dic.values())

# 입출력 예시
print(solution("Programmers"))


## 더 쉬운 풀이 (string 라이브러리와 dict.fromkeys 함수 사용)
# import string
# def solution(my_string):
#     count = dict.fromkeys(string.ascii_uppercase + string.ascii_lowercase, 0)
#     for s in my_string:
#         count[s] += 1
#     return list(count.values())