# https://school.programmers.co.kr/learn/courses/30/lessons/42888

from collections import defaultdict

def solution(record):
    uid_dic = defaultdict(str)
    action_expression = ["들어왔습니다.", "나갔습니다."]
    result = []
    
    for action in record:
        action = action.split(" ")
        if action[0] == "Enter":  # 입장시 uid에 닉네임 기록
            result.append((0, action[1]))
            uid_dic[action[1]] = action[2]
        elif action[0] == "Leave":
            result.append((1, action[1]))
        elif action[0] == "Change":  # 닉네임 변경시 uid에 갱신
            uid_dic[action[1]] = action[2]
    
    # 문구 변환 및 uid를 통한 닉네임 검색
    for i in range(len(result)):
        result[i] = str(uid_dic[result[i][1]]) + "님이 " + action_expression[result[i][0]]
    
    return result

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))