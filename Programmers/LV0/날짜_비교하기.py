# https://school.programmers.co.kr/learn/courses/30/lessons/181838

def solution(date1, date2):
    # 리스트간 크기 비교가 가능
    return int(date1 < date2)

# 입출력 예시
print(solution([2021, 12, 28], [2021, 12, 29]))
print(solution([1024, 10, 24], [1024, 10, 24]))