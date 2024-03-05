# https://school.programmers.co.kr/learn/courses/30/lessons/159994

from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    c1, c2 = cards1.popleft(), cards2.popleft()
    for i in goal:
        if i == c1:
            if cards1:
                c1 = cards1.popleft()
        elif i == c2:
            if cards2:
                c2 = cards2.popleft()
        else:
            return "No"
    return "Yes"

# 입출력 예시
print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))