def solution(my_string, is_suffix):
    if my_string[-len(is_suffix):] == is_suffix :
        return 1
    return 0

# 입출력 예시
print(solution("banana", "ana"))
print(solution("banana", "nan"))
print(solution("banana", "wxyz"))
print(solution("banana", "abanana"))