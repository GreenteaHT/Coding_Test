# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def check_same(arr, x, y, size):
    initial = arr[x][y]
    for i in range(x, x + size):
        for j in range(y, y +size):
            if arr[i][j] != initial:
                return False
    return True

def quad_zip(arr, x, y, size):
    if check_same(arr, x, y, size):
        if arr[x][y] == 1:
            return [0, 1]
        else:
            return [1, 0]
    
    # 4분면으로 나누어서 재귀
    half_size = size // 2
    top_left = quad_zip(arr, x, y, half_size)
    top_right = quad_zip(arr, x, y + half_size, half_size)
    bottom_left = quad_zip(arr, x + half_size, y, half_size)
    bottom_right = quad_zip(arr, x + half_size, y + half_size, half_size)
    
    return [top_left[0] + top_right[0] + bottom_left[0] + bottom_right[0],
            top_left[1] + top_right[1] + bottom_left[1] + bottom_right[1]]
            
def solution(arr):
    return quad_zip(arr, 0, 0, len(arr))

# 입출력 예시
arr1 = [
    [1,1,0,0],
    [1,0,0,0],
    [1,0,0,1],
    [1,1,1,1]
    ]
arr2 = [
    [1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1],
    [0,0,0,0,1,1,1,1],
    [0,1,0,0,1,1,1,1],
    [0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,1,0,0,1],
    [0,0,0,0,1,1,1,1]
    ]

print(solution(arr1))  # [4, 9]
print(solution(arr2))  # [10, 15]