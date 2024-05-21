# https://school.programmers.co.kr/learn/courses/30/lessons/12946

def hanoi(n, start, end, mid, moves):
    # 제일 작은 원판의 이동
    if n == 1:
        moves.append([start, end])
    else:
        # n-1개의 원판 이동
        hanoi(n-1, start, mid, end, moves)
        # n개 중 제일 밑에있는 큰 원 판 이동
        moves.append([start, end])
        # 이동한 큰 원판에 n-1개의 원판 다시 순서대로 쌓기
        hanoi(n-1, mid, end, start, moves)

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer

# 입출력 예시
print(solution(2))
print(solution(3))
        
