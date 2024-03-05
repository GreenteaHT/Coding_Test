# https://school.programmers.co.kr/learn/courses/30/lessons/181834

import re

def solution(myString):
    return re.sub("[a-k]", 'l', myString)

# 입출력 예시
print(solution("abcdevwxyz"))
print(solution("jjnnllkkmm"))


# maketrans 이용
# def solution(myString):
#     return myString.translate(str.maketrans('abcdefghijk', 'lllllllllll'))

# 알파벳의 크기 비교
# def solution(myString):
#     answer = [x if x > 'l' else 'l' for x in myString]
#     return ''.join(answer)