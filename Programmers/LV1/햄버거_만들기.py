# https://school.programmers.co.kr/learn/courses/30/lessons/133502

# def solution(ingredient):
#     ing_str = ''.join(map(str, ingredient))
#     answer = 0
#
#     while "1231" in ing_str:
#         ing_str = ing_str.replace("1231", '', 1)
#         answer += 1
#     return answer

def solution(ingredient):
    answer = 0
    for i in range(len(ingredient)):
        flg1 = 0
        n = 0
        while n < len(ingredient):
            if ingredient[n] == 1:
                if ingredient[n + 1:n + 4] == [2, 3, 1]:
                    answer += 1
                    del ingredient[n: n + 4]
                    n -= 1
                    flg1 = 1
                    break
            n += 1
        if not flg1:
            break
    return answer

# 입출력 예시
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1, 1, 2, 3, 1]))

