# https://school.programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    A.sort()
    B.sort()
    
    # 투포인터 이용
    pointerA = 0
    pointerB = 0
    score = 0
    while pointerA < len(A) and pointerB < len(B):
        # A의 현재 남아있는 가장 남은 값을 넘는 B를 찾음
        if A[pointerA] < B[pointerB]:
            score += 1
            pointerA += 1
        pointerB += 1
    
    return score

print(solution([5, 1, 3, 7], [2, 2, 6, 8]))