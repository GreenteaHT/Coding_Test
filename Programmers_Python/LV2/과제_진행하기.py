# https://school.programmers.co.kr/learn/courses/30/lessons/176962

from collections import deque

def solution(plans):
    stack = deque([])
    answer = []
    plans = [[i[0], int(i[1][0:2]) * 60 + int(i[1][3:5]), int(i[2])] for i in plans]
    plans.sort(key=lambda x: x[1])
    print(plans)
    
    process = plans[0]

    # 주어진 과제 진행
    for i in range(1, len(plans)):
        current_time = plans[i][1]
        usable_time = current_time - process[1]
        
        if usable_time < process[2]:  # 현재 과제를 완료 하지 못할 때
            stack.append([process[0], process[1], process[2] - usable_time])
        else:  # 현재 과제를 완료 했을 떄
            answer.append(process[0])
            usable_time -= process[2]
            # 남은 과제 풀기
            while usable_time >= 0 and stack:
                sub, start, time = stack.pop()
                if usable_time < time: # 남은 과제도 풀지 못할 시
                    stack.append([sub, start, time - usable_time])
                else:  # 남은 과제를 풀었을 시
                    answer.append(sub)
                usable_time -= time
        
        process = plans[i]
    
    # 마지막 과제
    answer.append(process[0])
    # 남은 과제
    while stack:
        answer.append(stack.pop()[0])
        
    return answer


# 입출력 예시
print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
