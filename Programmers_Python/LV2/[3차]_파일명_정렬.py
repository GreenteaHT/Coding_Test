# https://school.programmers.co.kr/learn/courses/30/lessons/17686

import re

def solution(files):

    
    # 파일명을 HEAD, NUMBER, TAIL로 나누는 함수
    def parse(file):
        match = re.match(r"([^\d]+)(\d{1,5})(.*)", file)
        head = match.group(1)
        number = match.group(2)
        tail = match.group(3)
        return (head, number, tail)
    
    # 정렬 기준에 맞춰 정렬
    files.sort(key=lambda file: (parse(file)[0].lower(), int(parse(file)[1])))
    
    return files

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))


## 딕셔너리로 풀려고 했지만 효율적이지 않은 것 같음
# from collections import defaultdict

# def solution(files):
#     dic = defaultdict(list)
#     answer = []
    
#     for n, file in enumerate(files):
#         i = 0
#         # 헤드 분리
#         head = ''
#         while not file[i].isdigit():
#             head += file[i]
#             i += 1
#         # 숫자 분리
#         number = ''
#         while file[i].isdigit():
#             number += file[i]
#             i += 1
#         # 테일 분리
#         tail = file[i:]
#         # 딕셔너리에 저장
#         dic[head.upper()].append((int(number), n, file))
    
#     # 키를 사전순으로 정렬
#     dic = sorted(dic.items())
    
#     # 키 순서로 출력 및 값 순서로 정렬
#     for head in dic:
#         number = sorted(head[1], key=lambda x:(x[0], x[1]))
#         for file in number:
#             answer.append(file[2])
   
#     return answer