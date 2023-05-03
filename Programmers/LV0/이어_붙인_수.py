# https://school.programmers.co.kr/learn/courses/30/lessons/181928

def solution(num_list):
    even_sum = 0
    odd_sum = 0
    for i in num_list:
        if i % 2 == 0:
            # 앞자리 부터 이어붙이므로, 더하기 전에 10을 곱해줌
            even_sum *= 10
            even_sum += i
        else:
            odd_sum *= 10
            odd_sum += i
    return even_sum + odd_sum

# 입출력 예시
print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))
