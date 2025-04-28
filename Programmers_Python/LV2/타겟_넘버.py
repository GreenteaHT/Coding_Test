# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    current_sums = [0]
    next_sums = []

    for num in numbers:
        for accumulated_sum in current_sums:
            next_sums.append(accumulated_sum + num)
            next_sums.append(accumulated_sum - num)
        current_sums, next_sums = next_sums, []

    return current_sums.count(target)

# 입출력 예시
print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 2))
