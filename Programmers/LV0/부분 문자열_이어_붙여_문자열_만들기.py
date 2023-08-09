# https://school.programmers.co.kr/learn/courses/30/lessons/181911

def solution(my_strings, parts):
    answer = ''
    for wrd, rng in zip(my_strings, parts):
        answer += wrd[rng[0]:rng[1]+1]
    return answer

# 입출력 예시
print(solution(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))