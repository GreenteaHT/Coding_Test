# https://school.programmers.co.kr/learn/courses/30/lessons/181921

def solution(l, r):
    r_lst = []
    # r을 바이너리 값으로 변환 (5이상은 1, 5미만은 0)
    r_binary = int(''.join([str(int(i) // 5) for i in str(r)]), 2)
    for i in range(1, r_binary+1):
        # 바이너리 값을 5로 이루어진 정수로 치환
        case_5 = int(str(bin(i))[2:]) * 5
        # l보다 크거나 같을 경우에만 추가
        if case_5 >= l:
            r_lst.append(case_5)
    return r_lst if r_lst else [-1]


# 입출력 예시
print(solution(5, 555))
print(solution(10, 20))