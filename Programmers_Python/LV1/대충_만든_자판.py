# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    alp_map_lst = [101]*26
    for str_key in keymap:
        for n, wrd_key in enumerate(str_key):
            ord_tmp = ord(wrd_key) - 65
            alp_map_lst[ord_tmp] = min(n + 1, ord_tmp)

    lst = []
    for str_trg in targets:
        cnt = 0
        for wrd_trg in str_trg:
            ord_tmp = ord(wrd_trg)-65
            if alp_map_lst[ord_tmp] == 101:
                cnt = -1
                break
            cnt += alp_map_lst[ord_tmp]
        lst.append(cnt)
    return lst

# 입출력 예시
print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
print(solution(["AA"], ["B"]))
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))