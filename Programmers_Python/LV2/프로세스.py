# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    pri_dic = {}
    for n, i in enumerate(priorities):
        pri_dic[i] = pri_dic.get(i, []) + [n]
    pri_order_list = sorted(pri_dic.keys(), reverse=True)

    # answer = 0
    # cursor = 0
    # for j in pri_order_list:
    #     if j == priorities[location]:
    #         c = 1
    #         # 커서의 위치랑 location의 위치를 통한 몇번째인지 확인
    #     else:
    #         answer += len(pri_dic[j])
    #         cursor = max(k for k in pri_dic[j] if cursor < k ) if pri_dic[j][0] < cursor else pri_dic[j][-1]


    pri_que = deque(priorities)
    answer = 0
    track_loaction = location
    for i in pri_order_list:
        cnt2 = 0
        while cnt2 < len(pri_dic[i]):
            if location == 0 and priorities[location] == i:
                return answer + 1

            tmp = pri_que.popleft()
            if tmp != i:
                pri_que.append(tmp)
            else:
                cnt2 += 1
                answer += 1

            location = location - 1 if location != 0 else len(pri_que) - 1
    return pri_que


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))