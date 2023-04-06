# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    # 각 학생이 소지한 체육복 개수를 리스트에 정리
    cloth_lst = [1] * n

    for i in lost:
        cloth_lst[i - 1] -= 1
    for i in reserve:
        cloth_lst[i - 1] += 1

    # 체육복이 없는 학생이 여분을 가진 학생에게 빌리기
    for i in range(n):
        if cloth_lst[i] == 0:
            if i > 0 and cloth_lst[i - 1] == 2:
                cloth_lst[i] += 1
                cloth_lst[i - 1] -= 1
            elif i < n - 1 and cloth_lst[i + 1] == 2:
                cloth_lst[i] += 1
                cloth_lst[i + 1] -= 1
    
    # 체육복의 개수가 하나 이상인 학생의 수만 구하기
    return sum([1 for i in cloth_lst if i > 0])

# 입출력 예시
print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
