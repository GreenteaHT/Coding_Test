#https://school.programmers.co.kr/learn/courses/30/lessons/181897

def solution(n, slicer, num_list):
    a, b, c = slicer[0], slicer[1], slicer[2]
    if n == 1:
        return num_list[0:b+1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b+1]
    elif n == 4:
        return num_list[a:b+1:c]

# 입출력 예시
print(solution(3, [1, 5,2], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(solution(4, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]))