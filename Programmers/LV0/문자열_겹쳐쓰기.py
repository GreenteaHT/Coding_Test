# https://school.programmers.co.kr/learn/courses/30/lessons/181943

def solution(my_string, overwrite_string, s):
	# 슬라이싱 사용
	return my_string[:s] + overwrite_string \
            + my_string[s+len(overwrite_string):]

# 입출력 예시
print(solution("He11oWor1d", "lloWorl", 2))
print(solution("Program29b8UYP", "merS123", 7))
