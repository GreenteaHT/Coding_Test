# https://school.programmers.co.kr/learn/courses/30/lessons/12927

def solution(works, n):
    works_cnt = len(works)
    overtime = sum(works) - n
    # 제일 작업량이 많은 일부터 1씩 줄여야하므로 결과적으론 모든 작업량을 더하고 작업개수로 나누는 것과 같다.
    # 기본적으로 몫 만큼의 작업이 존재하고 나머지의 개수만큼 몫 + 1의 작업량이 존재한다.
    print(((overtime//works_cnt) ** 2) * (works_cnt - overtime%works_cnt))
    print(((overtime//works_cnt + 1) ** 2) * (overtime%works_cnt))
    return ((overtime//works_cnt) ** 2) * (works_cnt - overtime%works_cnt) + ((overtime//works_cnt + 1) ** 2) * (overtime%works_cnt)

# 입출력 예시
print(solution([4, 3, 3], 4))