# https://school.programmers.co.kr/learn/courses/30/lessons/181851

def solution(rank, attendance):
    a = [i for i in range(len(rank))]
    # attendance가 true 일때만 인덱스와 한 쌍으로 묶어서 저장
    # 정렬을 하고, 인덱스를 이용하지 않기 때문에 리스트로 정리해도 됨
    dic = {ra: i for i, ra, at in zip(a, rank, attendance) if at}
    dic = sorted(dic.items())
    return dic[0][1] * 10000 + dic[1][1] * 100 + dic[2][1]

# 입출력 예시
print(solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False]))
print(solution([1, 2, 3], [True, True, True]))
print(solution([6, 1, 5, 2, 3, 4], [True, False, True, False, False, True]))