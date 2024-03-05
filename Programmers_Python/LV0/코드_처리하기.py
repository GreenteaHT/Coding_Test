# https://school.programmers.co.kr/learn/courses/30/lessons/181932

def solution(code):
    mode = 0
    ret = ''
    for idx, i in enumerate(code):
        if i == '1':
            mode = 0 if mode else 1
        else:
            # mode 가 0일때 짝수, mode 가 1일때 홀수 이므로
            if idx % 2 == mode:
                ret += i
    # ret가 비었다면 "EMPTY" 반환
    return ret if ret else "EMPTY"

# 입출력 예시
print(solution("abc1abc1abc"))