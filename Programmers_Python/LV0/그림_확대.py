# https://school.programmers.co.kr/learn/courses/30/lessons/181836

def solution(picture, k):
    Height = len(picture)
    Width = len(picture[0])
    answer = [""]*(Height*k)

    for h in range(Height):
        for w in range(Width):
            pix = picture[h][w]
            for i in range(k):
                answer[h*k + i] += pix * k
    return answer

# 입출력 예시
print(solution([".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."], 2))
print(solution(["x.x", ".x.", "x.x"], 3))