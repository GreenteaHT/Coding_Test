# https://school.programmers.co.kr/learn/courses/30/lessons/181900

def solution(my_string, indices):
    cnt = 0
    for i in sorted(indices):
        # indices의 인덱스의 밀림 방지
        i -= cnt
        cnt += 1
        # 문자열 슬라이싱을 통한 특정 인덱스 문자 제거
        my_string = my_string[:i] + my_string[i+1:]
    return my_string

# 입출력 예시
print(solution("apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3]))