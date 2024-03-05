# https://school.programmers.co.kr/learn/courses/30/lessons/181846

def solution(a, b):
    # eval을 사용하여도 어차피 정수연산을 하기 때문에 형변환 과정이 들어있어 연산시간이 비슷함
    # return str(eval(a + "+" + b))
    return str(int(a) + int(b))

# 입출력 예시
print(solution("582", "734"))
print(solution("18446744073709551615", "287346502836570928366"))
print(solution("0", "0"))