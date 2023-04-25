# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    cnt = 0
    for i in range(len(s)):
        stack_lst = []
        a = s[i:] + s[:i]
        for i in a:
            if i == '(' or i == '[' or i == '{':
                stack_lst.append(i)
            elif stack_lst:
                if i == ')':
                    if stack_lst[-1] == '(':
                        stack_lst.pop()
                    else:
                        stack_lst.append(i)
                elif i == ']':
                    if stack_lst[-1] == '[':
                        stack_lst.pop()
                    else:
                        stack_lst.append(i)
                elif i == '}':
                    if stack_lst[-1] == '{':
                        stack_lst.pop()
                    else:
                        stack_lst.append(i)
            else:
                stack_lst.append(i)
        if not stack_lst:
            cnt += 1
    return cnt

# 입출력 예시
print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))