# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i, n in enumerate(numbers):
        while stack and numbers[stack[-1]] < n:
            answer[stack.pop()] = n
        stack.append(i)
        
    return answer

# 입출력 예시
print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))