# https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    answer = []
    mode_list = ["code", "date", "maximum", "remain"]
    mode = mode_list.index(ext)
    # 데이터 추출
    for d in data:
        if d[mode] < val_ext:
            answer.append(d)
    # 데이터 정렬
    answer.sort(key=lambda a: a[mode_list.index(sort_by)])
    return answer

# 입출력 예시
print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))