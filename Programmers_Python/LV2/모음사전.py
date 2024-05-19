# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    # 각 자릿수에서 뒤에 올 수 있는 단어 개수
    word_cnt = [781, 156, 31, 6, 1]
    
    # 각 자리에 있는 철자로 계산
    position = 0
    for i, char in enumerate(word):
        position += vowels.index(char) * word_cnt[i] + 1
    
    return position

# 입출력 예시
print(solution("AAAAE"))  # 6
print(solution("AAAE"))   # 10
print(solution("I"))      # 1563
print(solution("EIO"))    # 1189