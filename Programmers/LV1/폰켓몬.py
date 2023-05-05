# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    # set을 이용해 최대 종류가 몇개인지 확인
    # 최대 종류가 N/2 보다 많으면 최대 N/2개 밖에 못가져가므로, N/2 반환
    return min(len(nums) / 2, len(set(nums)))

# 입출력 예시
print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))