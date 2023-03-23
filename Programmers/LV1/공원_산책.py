# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    H = len(park)
    W = len(park[0])
    dir_dic = {"E": [0, 1], "W": [0, -1], "N": [-1, 0], "S": [1, 0]}

    yx = [0, 0]
    for i in range(W):
        for j in range(H):
            if park[j][i] == "S":
                yx = [j, i]
                break

    for i in routes:
        flg1 = False
        dir, dis = i.split(' ')
        dis = int(dis)
        if 0 <= yx[1] + dir_dic[dir][1] * dis < W and 0 <= yx[0] + dir_dic[dir][0] * dis < H:
            for x in range(yx[1]+1, yx[1] + dir_dic[dir][1] * dis + 1):
                if not park[yx[0]][x] == "O":
                    flg1 = True
                    break
            for y in range(yx[0]+1, yx[0] + dir_dic[dir][0] * dis + 1):
                if not park[y][yx[1]] == "O":
                    flg1 = True
                    break
            if not flg1:
                yx[0] += dir_dic[dir][0] * dis
                yx[1] += dir_dic[dir][1] * dis
    return yx

# 입출력 예시
print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]	))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))