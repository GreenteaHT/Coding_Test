#https://school.programmers.co.kr/learn/courses/30/lessons/181874

def solution(myString):
    myString = myString.lower()
    return myString.replace('a', 'A')
    # import re
    # return re.sub("a", "A", myString)

# 입출력 예시
print(solution("abstract algebra"))
print(solution("PrOgRaMmErS"))