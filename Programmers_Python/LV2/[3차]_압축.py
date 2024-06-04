# https://school.programmers.co.kr/learn/courses/30/lessons/17684

from string import ascii_uppercase

def solution(msg):
    dic = {alp: num for num, alp in enumerate(ascii_uppercase, 1)}
    w = ""
    index = 26
    output = []
    
    for c in msg:
        if w + c in dic:
            w += c
        else:
            output.append(dic[w])
            index += 1
            dic[w + c] = index
            w = c
    output.append(dic[w])
 
    return output

# 테스트
print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))