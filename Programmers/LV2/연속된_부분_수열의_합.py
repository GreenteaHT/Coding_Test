# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    seq_len = len(sequence)

    for i in range(seq_len):
        if sequence[seq_len - i] == k:
            return [seq_len-i, seq_len-i]
        elif sequence[seq_len - i] < k:
            sequence = sequence[:seq_len-i]
            seq_len = len(sequence)
            break




    answer = []
    return answer

# 입출력 예시
print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))
