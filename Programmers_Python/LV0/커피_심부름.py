# https://school.programmers.co.kr/learn/courses/30/lessons/181837

def solution(order):
    cost = 0
    for menu in order:
        if "americano" in menu:
            cost += 4500
        elif "cafelatte" in menu:
            cost += 5000
        else:
            cost += 4500
    return cost

# 입출력 예시
print(solution(["cafelatte", "americanoice", "hotcafelatte", "anything"]))
print(solution(["americanoice", "americano", "iceamericano"]))