# https://school.programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict

def solution(genres, plays):
    answer = []

    # 장르: [총 플레이 수, [플레이 수, 고유번호]]
    genres_dict = defaultdict(lambda: [0, []])
    # genres_dict = dic.get(genres[i], [0, []]) + ... 응용 가능
    for i in range(len(genres)):
        genres_dict[genres[i]][0] += plays[i]
        genres_dict[genres[i]][1].append([plays[i], i])

    # 총 플레이 수로 정렬
    for j in sorted(genres_dict.values(), reverse=True):
        cnt = 0
        # 장르 당 최대 두 개 까지만, 플레이 수는 내림차순, 고유번호는 오름차순
        for k in sorted(j[1], reverse=True, key=lambda x: (x[0], -x[1])):
            answer.append(k[1])
            cnt += 1
            if cnt == 2:
                break
    return answer

# 입출력 예시
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))