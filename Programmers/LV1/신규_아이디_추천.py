# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for c in "~!@#$%^&*()=+[{]}:?,<>/":
        new_id = new_id.replace(c, '')
    # 3단계
    import re
    new_id = re.sub('([.]+)', '.', new_id)
    # 4단계
    if new_id[:1] == '.':
        new_id = new_id[1:]
    if new_id[-1:] == '.':
        new_id = new_id[:-1]
    # 5단계
    if new_id == '':
        new_id = 'a'
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1:] == '.':
        new_id = new_id[:-1]
    # 7단계
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id

# 입출력 예시
print(solution(	"...!@BaT#*..y.abcdefghijklm"))
print(solution(	"z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))


## 정규표현식 이용
# import re
#
# def solution(new_id):
#     # 1단계
#     new_id = new_id.lower()
#     # 2단계
#     new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
#     # 3단계
#     new_id = re.sub('([.]{2,})', '.', new_id)
#     # 4단계
#     new_id = re.sub('^[.]|[.]$', '', new_id)
#     # 5단계
#     if new_id == '':
#         new_id = 'a'
#     # 6단계
#     new_id = re.sub('[.]$', '', new_id[:15])
#     # 7단계
#     new_id = new_id.ljust(3, new_id[-1])
#     return new_id