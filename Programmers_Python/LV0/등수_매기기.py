# https://school.programmers.co.kr/learn/courses/30/lessons/120882

def solution(score):
    score_len = len(score)
    subject_len = len(score[0])
    for i in range(score_len):
        score[i] = sum(score[i])/subject_len
    score_srt = sorted(score, reverse=True)

    answer = []
    for i in score:
        answer.append(score_srt.index(i)+1)
    return answer

# 입출력 예시
print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))