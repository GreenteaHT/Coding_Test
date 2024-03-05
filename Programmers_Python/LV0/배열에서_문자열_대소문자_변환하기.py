# https://school.programmers.co.kr/learn/courses/30/lessons/181875

def solution(strArr):
    for n, s in enumerate(strArr):
        if n % 2 != 0:
            strArr[n] = s.upper()
        else:
            strArr[n] = s.lower()
    return strArr

# 입출력 예시    
print(solution(["AAA","BBB","CCC","DDD"]))
print(solution(["aBc","AbC"]))