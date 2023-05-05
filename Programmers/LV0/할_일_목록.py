# https://school.programmers.co.kr/learn/courses/30/lessons/181885?language=python3

def solution(todo_list, finished):
    return [a for a, b in zip(todo_list, finished) if not b]

print(solution(["problemsolving", "practiceguitar", "swim", "studygraph"], [True, False, True, False]))


