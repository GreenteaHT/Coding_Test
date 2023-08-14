# https://school.programmers.co.kr/learn/courses/30/lessons/181921

def solution(l, r):
    r_lst = []
    # r을 바이너리 값으로 변환 (5이상은 1, 5미만은 0)
    str_r = str(r)
    len_str_r = len(str_r)
    r_binary = 2 ** len_str_r - 1
    for n, i in enumerate(str_r):
        if int(i) == 0:
            r_binary -= 2 ** (len_str_r - n - 1)
        elif int(i) < 5:
            r_binary -= 2 ** (len_str_r - n - 1)
            break
        
    for i in range(1, r_binary+1):
        # 바이너리 값을 5로 이루어진 정수로 치환
        case_5 = int(str(bin(i))[2:]) * 5
        # l보다 크거나 같을 경우에만 추가
        if case_5 >= l:
            r_lst.append(case_5)
    return r_lst or [-1]

# 입출력 예시
print(solution(5, 4500))
print(solution(1, 100))