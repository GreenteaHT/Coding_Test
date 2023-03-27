# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    ing_stk = []
    n_hambuger = 0

    for i in ingredient:
        ing_stk.append(i)
        if ing_stk[-4:] == [1, 2, 3, 1]:
            n_hambuger += 1
            del ing_stk[-4:]
    return n_hambuger

# 입출력 예시
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))

