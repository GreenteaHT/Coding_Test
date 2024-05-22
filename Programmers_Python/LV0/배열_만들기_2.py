# https://school.programmers.co.kr/learn/courses/30/lessons/181921

def solution(l, r):
    n_lst = []
    n_binary = 2 ** len(str(r))
    
    # r을 바이너리 값으로 변환 (5 -> 1, 0 -> 0)
    for i in range(1, n_binary):
        # 바이너리 값을 5로 이루어진 정수로 치환
        case_5 = int(bin(i)[2:]) * 5
        if case_5 >= l and case_5 <= r:
            n_lst.append(case_5)
    return n_lst or [-1]

# 테스트 예시
print(solution(5, 555))  # [5, 50, 55, 500, 505, 550, 555]
print(solution(10, 20))  # [-1]