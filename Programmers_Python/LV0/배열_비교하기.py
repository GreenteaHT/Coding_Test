# https://school.programmers.co.kr/learn/courses/30/lessons/181856

def solution(arr1, arr2):
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    if len_arr1 == len_arr2:
        sum_arr1 = sum(arr1) 
        sum_arr2 = sum(arr2)
        if sum_arr1 == sum_arr2:
            return 0 
        elif sum_arr1 > sum_arr2:
            return 1
        else:
            return -1
    elif len_arr1 > len_arr2:
        return 1
    else:
        return -1

# 입출력 예시    
print(solution([49, 13], [70, 11, 2]))
print(solution([100, 17, 84, 1], [55, 12, 65, 36]))
print(solution([1, 2, 3, 4, 5], [3, 3, 3, 3, 3]))
