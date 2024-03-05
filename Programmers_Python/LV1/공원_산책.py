# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    H = len(park)
    W = len(park[0])
    dir_dic = {"E": [0, 1], "W": [0, -1], "N": [-1, 0], "S": [1, 0]}

    cur_pos = None
    for i in range(W):
        for j in range(H):
            if park[j][i] == "S":
                cur_pos = [j, i]
                break
        if cur_pos is not None:
            break

    for i in routes:
        dir, dis = i.split(' ')
        dis = int(dis)
        new_pos = [cur_pos[0] + dir_dic[dir][0] * dis, cur_pos[1] + dir_dic[dir][1] * dis]

        if 0 <= new_pos[1] < W and 0 <= new_pos[0] < H:
            flg1 = False
            for j in range(dis):
                tmp_pos = [cur_pos[0] + dir_dic[dir][0] * (j+1), cur_pos[1] + dir_dic[dir][1] * (j+1)]
                if park[tmp_pos[0]][tmp_pos[1]] == "X":
                    flg1 = True
                    break
            if not flg1:
                cur_pos = new_pos
    return cur_pos

# 입출력 예시
print(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]))
print(solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]))
print(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]))
