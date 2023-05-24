# https://school.programmers.co.kr/learn/courses/30/lessons/181862

import re

def solution(myStr):
    # re.split을 이용한 분리, filter를 이용한 빈 문자열 제거
    answer = list(filter(None, re.split('[abc]', myStr)))
    # 리스트가 비어있다면
    if not answer:
        return ["EMPTY"]
    return answer

# 입출력 예시
print(solution("baconlettucetomato"))
print(solution("abcd"))
print(solution("cabab"))