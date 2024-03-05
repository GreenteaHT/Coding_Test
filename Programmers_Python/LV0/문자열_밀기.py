# https://school.programmers.co.kr/learn/courses/30/lessons/120921

def solution(A, B):
    # for i in range(len(A)):
    #     if B == A[-i:] + A[:-i]:
    #         return i

    return (B*2).find(A)

# 입출력 예시
print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution("atat", "tata"))
print(solution("abc", "abc"))