# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    ing_str = ''.join(map(str, ingredient))
    answer = 0

    while "1231" in ing_str:
        ing_str = ing_str.replace("1231", '', 1)
        answer += 1
    return answer

# 입출력 예시
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1, 1, 2, 3, 1]))