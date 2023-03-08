# https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling):
    wrd_lst3 = ["aya", "woo"]
    wrd_lst2 = ["ye", "ma"]
    answer = 0
    for bab in babbling:
        len_cnt = 0
        for wrd in wrd_lst3:
            if wrd in bab:
                len_cnt += 3
        for wrd in wrd_lst2:
            if wrd in bab:
                len_cnt += 2
        if len(bab) == len_cnt:
            answer += 1
    return answer

# 입출력 예시
print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))