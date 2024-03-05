# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    alp_lst = [chr(i) for i in range(97, 123)]
    answer = ''

    for i in skip:
        alp_lst.remove(i)

    alp_len = len(alp_lst)
    for j in s:
        answer += alp_lst[(alp_lst.index(j) + index) % alp_len]
    return answer

# 입출력 예시
print(solution("aukks", "wbqd", 5))
