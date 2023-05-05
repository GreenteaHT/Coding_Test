# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    # 덧셈한 값을 저장한 리스트 할당(이전 리스트 저장)
    pre_cost_lst = triangle[0].copy()
    # 깊이 2부터 루프문 활용
    for i in triangle[1:]:
        degree = len(i)
        # 덧셈한 값을 저장할 리스트 할당
        cost_lst = [0] * degree
        tmp = 0
        for j in range(degree-1):
            # 왼쪽 루트 요소와의 합과 이전과정에서 오른쪽 루트 요소와의 합을 비교하여 저장
            cost_lst[j] = max(pre_cost_lst[j] + i[j], tmp)
            # 오른쪽 루트 요소와의 합을 임시 저장
            tmp = pre_cost_lst[j] + i[j+1]
        # 왼쪽부터 차례로 더했을때 마지막 경우
        cost_lst[-1] = tmp
        # 현재 덧셈을 저장한 리스트를 이전 리스트로
        pre_cost_lst = cost_lst.copy()
    return max(pre_cost_lst)

# 입출력 예시
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))