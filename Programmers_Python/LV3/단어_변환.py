# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    # BFS
    queue = deque([(begin, 0)])  # (단어, 변환 단계)
    visited = set(begin)
    
    while queue:
        current_word, step = queue.popleft()
        
        if current_word == target:
            return step
        
        for word in words:
            if word not in visited and is_one_letter_diff(current_word, word):
                visited.add(current_word)
                queue.append((word, step + 1))

    return 0

# 단어가 한단어 차이인지 확인하는 함수
def is_one_letter_diff(word1, word2):
    cnt = 0
    for spell1, spell2 in zip(word1, word2):
        if spell1 != spell2:
            cnt += 1
        if cnt > 1:
            return False
    return cnt == 1

# 테스트
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))  # 출력: 4

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))  # 출력: 0