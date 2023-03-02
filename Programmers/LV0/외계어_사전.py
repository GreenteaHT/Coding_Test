# https://school.programmers.co.kr/learn/courses/30/lessons/120869

def solution(spell, dic):
    spell_len = len(spell)
    for wrd in dic:
        if spell_len != len(wrd):
            continue
        flg = True
        for s in spell:
            if wrd.count(s) != 1:
                flg = False
                break
        if flg:
            return 1
    return 2

# 입출력 예시
print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))