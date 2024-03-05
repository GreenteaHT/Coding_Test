# https://school.programmers.co.kr/learn/courses/30/lessons/181915

def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer

# 입출력 에시
print(solution("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))
print(solution("zpiaz", [1, 2, 0, 0, 3]))
