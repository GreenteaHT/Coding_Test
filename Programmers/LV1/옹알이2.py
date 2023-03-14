# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    answer = 0
    for b in babbling:
        for wrd in ["aya", "ye", "woo", "ma"]:
            if wrd * 2 not in b:
                b = b.replace(wrd, ' ')
        if len(b.strip()) == 0:
            answer += 1
    return answer

# 입출력 예시
print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
