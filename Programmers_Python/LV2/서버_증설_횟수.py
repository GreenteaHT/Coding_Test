# https://school.programmers.co.kr/learn/courses/30/lessons/389479

def solution(players, m, k):
    server_table = [0] * 24
    active_server_count = 0

    for i, CCU in enumerate(players):  # CCU(Concurrent connected User)
        active_server_count -= server_table[i - k] if i >= k else 0
        required_server_count = CCU // m

        if required_server_count > active_server_count:
            server_table[i] = required_server_count - active_server_count
            active_server_count += server_table[i]

    return sum(server_table)

# 입출력 예시
print(solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5))   # 7
print(solution([0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0], 5, 1))  # 11
print(solution([0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 1, 1))  # 12