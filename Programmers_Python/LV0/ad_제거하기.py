# https://school.programmers.co.kr/learn/courses/30/lessons/181870

def solution(strArr):
    # answer = []
    # for i in strArr:
    #     if "ad" not in i:
    #         answer.append(i)
    # return answer
    return [word for word in strArr if 'ad' not in word]

# 입출력 예시
print(solution(["and","notad","abcd"]))
print(solution(["there","are","no","a","ds"]))