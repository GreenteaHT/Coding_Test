# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    elements_length = len(elements)
    answer = set()
    # i부터 시작한 길이 j의 연속 부분 수열
    # sum을 매번 호출하는것보다 alu를 만들어서 하나씩 더해가는것이 훨씬 빠름
    for i in range(elements_length):
        alu = elements[i]
        answer.add(alu)
        for j in range(i + 1, i + elements_length):
            alu += elements[j%elements_length]
            answer.add(alu)
    return len(answer)