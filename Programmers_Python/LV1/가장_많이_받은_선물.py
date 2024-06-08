# https://school.programmers.co.kr/learn/courses/30/lessons/258712

def solution(friends, gifts):
    n = len(friends)
    dic = {key:i for i, key in enumerate(friends)}  # 각 친구들의 해시 값
    exchange_table = [[0] * n for _ in range(n)]  # 주고받은 선물 표
    present_indi = [0] * n  # 선물 지수 표
    
    for sending in gifts:
        a, b = sending.split(' ')
        exchange_table[dic[a]][dic[b]] += 1
        present_indi[dic[a]] += 1
        present_indi[dic[b]] -= 1

    max_cnt = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if exchange_table[i][j] - exchange_table[j][i] == 0 and present_indi[i] >  present_indi[j] or exchange_table[i][j] > exchange_table[j][i]:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

    return max_cnt


# 입출력 예시
print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
print(solution(["joy", "brad", "alessandro", "conan", "david"],	["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))