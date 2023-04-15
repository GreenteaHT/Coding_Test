# https://school.programmers.co.kr/learn/courses/30/lessons/181187

def solution(r1, r2):
    cnt = 0
    for i in range(1, r2):
        dif1s = (r1**2 - i**2) if r1 > i else 0
        dif1 = int(dif1s**0.5)
        dif2 = int((r2**2 - i**2)**0.5)
        cnt += dif2 - dif1 + (1 if dif1 ** 2 == dif1s else 0)
    cnt += 1
    return cnt * 4

# 입출력 예시
print(solution(2, 3))

