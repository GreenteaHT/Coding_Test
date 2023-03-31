# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    scheduler = []
    answer = []
    plans = [[i[0], int(i[1][0:2]) * 60 + int(i[1][3:5]), int(i[2])] for i in plans]
    plans.sort(key=lambda x: x[1])
    print(plans)

    def chk_solution():
        return 0

    for i in range(len(plans)-1):
        if plans[i+1][1] - plans[i][1] < plans[i][2]:
            plans[i][2] -= plans[i + 1][1] - plans[i][1]
            scheduler.append(plans[i])
        else:
            answer.append(plans[i][0])
            if scheduler:
                time = plans[i + 1][1] - plans[i][1] - plans[i][2]
                for s in scheduler:
                    if time > s[]



    return plans


# 입출력 예시
print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))