# https://school.programmers.co.kr/learn/courses/30/lessons/120913

def solution(my_str, n):
    # answer = [my_str[i*n:i*n+n] for i in range((len(my_str)+n-1)//n)]
    answer = list(map(''.join, zip(*[iter(my_str)]*n)))
    return answer

# 입출력 예시
print(solution("abc1Addfggg4556b", 6))
print(solution("abcdef123", 3))
