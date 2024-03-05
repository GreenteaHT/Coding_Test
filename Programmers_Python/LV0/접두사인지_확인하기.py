# https://school.programmers.co.kr/learn/courses/30/lessons/181906

def solution(my_string, is_prefix):
    if my_string[:len(is_prefix)] == is_prefix:
        return 1
    return 0

# 입출력 예시
print(solution("banana", "ban"))
print(solution("banana", "nan"))
print(solution("banana", "abcd"))
print(solution("banana", "bananan"))