# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    pos = [0, 0]
    way = set()

    for d in dirs:
        if d == 'U':
            if pos[1] < 5:
                way.add((pos[0], pos[1] + 0.5))
                pos[1] += 1
        elif d == 'D':
            if pos[1] > -5:
                way.add((pos[0], pos[1] - 0.5))
                pos[1] -= 1
        elif d == 'R':
            if pos[0] < 5:
                way.add((pos[0] + 0.5, pos[1]))
                pos[0] += 1
        elif d == 'L':
            if pos[0] > -5:
                way.add((pos[0] - 0.5, pos[1]))
                pos[0] -= 1
    return len(way)

# 입출력 예시
print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))