# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    s_lst = []
    cnt_lst = ['', 0, 0, '']
    for char in s:
        cnt_lst[3] += char

        if cnt_lst[0] == '':
            cnt_lst[0] = char

        if char == cnt_lst[0]:
            cnt_lst[1] += 1
        else:
            cnt_lst[2] += 1

        if cnt_lst[1] == cnt_lst[2]:
            s_lst.append(cnt_lst[3])
            cnt_lst = ['', 0, 0, '']

    if cnt_lst[3] is not '':
        s_lst.append(s[-1])

    return len(s_lst)

# 입출력 예시
print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))