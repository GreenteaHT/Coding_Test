# https://school.programmers.co.kr/learn/courses/30/lessons/49993
import copy

def solution(skill, skill_trees):
    skill_ord = list(skill)
    skill_dic = {key: [past_skill, False] for key, past_skill
                 in zip(skill_ord, [0] + skill_ord[:-1])}
    skill_dic[0] = [1, True]

    cnt = 0
    # 케이스-알파벳마다
    for skill_case in skill_trees:
        suc_flg = True
        tmp_skill_dic = copy.deepcopy(skill_dic)
        for i in skill_case:
            # 딕셔너리에 존재하는지?
            if i in tmp_skill_dic:
                # 이전 스킬을 배웠다면 스킬을 배움
                if tmp_skill_dic[tmp_skill_dic[i][0]][1]:
                    tmp_skill_dic[i][1] = True
                # 아니면 종료
                else:
                    suc_flg = False
                    break
        if suc_flg:
            cnt += 1
    return cnt

# 입출력 예시
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))