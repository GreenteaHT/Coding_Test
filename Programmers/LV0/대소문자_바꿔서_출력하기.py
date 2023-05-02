# https://school.programmers.co.kr/learn/courses/30/lessons/181949

str = input()
answer = ''
for s in str:
    answer += s.upper() if s.islower() else s.lower()
print(answer)

# swapcase() 함수 이용

# 입출력 예시
# aBcDeFg
