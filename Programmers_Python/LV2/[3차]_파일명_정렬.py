# https://school.programmers.co.kr/learn/courses/30/lessons/17686

from collections import defaultdict
import re

def solution(files):
    dic = defaultdict(list)
    
    
    for n, file in enumerate(files):
        i = 0
        # 헤드 분리
        head = ''
        while file[i].isalpha():
            head += file[i]
            i += 1
        # 숫자 분리
        number = ''
        while file[i].isdigit():
            number += file[i]
            i += 1
        # 테일 분리
        tail = file[i:]
        # 딕셔너리에 저장
        dic[head.upper()].append((number, n, file))
    
    # 키를 사전순으로 정렬
    dic = sorted(dic.items())
    
    # 키 순서로 출력 및 값 순서로 정렬
    
    
    answer = []
    return answer