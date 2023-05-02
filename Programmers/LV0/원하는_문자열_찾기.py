# https://school.programmers.co.kr/learn/courses/30/lessons/181878

def solution(myString, pat):
	# 만족하면 1을 반환, 만족하지 못하면 0을 반환
    return int(pat.lower() in myString.lower())
  
# 입출력 예시
print(solution("AbCdEfG", "aBc"))
print(solution("aaAA", "aaaaa"))
