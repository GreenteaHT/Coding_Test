# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    # 첫 문자에 대한 변수 설정
    words_lst = [words[0]]
    last_spell = words[0][-1]

    # 루프문을 통한 끝말잇기 조건 체크
    for nn, w in enumerate(words[1:]):
        # 전 글자의 끝과 앞 글자의 처음이 일치하고 글자가 중복되지 않을 때
        if w[0] == last_spell and w not in words_lst:
            last_spell = w[-1]
            words_lst.append(w)
        # 탈락자의 경우
        else:
            return [(nn + 1) % n + 1, (nn + 1) // n + 1]

    # 마지막 단어까지 탈락자가 없을 경우
    return [0, 0]

# 입출력 예시
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang",
          "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
