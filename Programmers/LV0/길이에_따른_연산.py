# https://school.programmers.co.kr/learn/courses/30/lessons/181879

def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        prod = 1
        for i in num_list:
            prod *= i
        return prod

# 입출력 예시
print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
print(solution([2, 3, 4, 5]))


# def solution(num_list):
#     if len(num_list) >= 11:
#         return eval('+'.join(list(map(str, num_list))))
#     else:
#         return eval('*'.join(list(map(str, num_list))))

# reduce도 찾아보기