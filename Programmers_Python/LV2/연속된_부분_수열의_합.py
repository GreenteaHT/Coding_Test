# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    length = len(sequence)
    start, end = 0, 0  # 포인터 두개 사용
    min_length = length + 1
    alu = 0
    answer = []
    
    # k값 보다 작으면 수열의 뒷부분을 늘림
    while end < length:
        alu += sequence[end]
        
        # k값을 초과하면 수열의 앞부분을 줄임
        while alu > k and start <= end:
            alu -= sequence[start]
            start += 1
        
        if alu == k:
            if end - start + 1 < min_length:
                min_length = end - start + 1
                answer = [start, end]
        
        end += 1
            
    return answer

# 입출력 예시
print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))
