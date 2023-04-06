# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    pla_dic = {key: i for i, key in enumerate(players)}

    for p in callings:
        c = pla_dic[p]
        pla_dic[p] -= 1
        pla_dic[players[c-1]] += 1
        players[c-1], players[c] = players[c], players[c-1]

    return players

# 입출력 예시
print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))