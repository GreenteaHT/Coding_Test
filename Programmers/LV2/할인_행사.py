# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    cnt = 0
    want_dic = {key: value for key, value in zip(want, number)}
    
    # 미리 10개길이의 카운트 딕셔너리를 생성
    for i in discount[:10]:
        if i in want_dic:
            want_dic[i] -= 1
        
        # 모든 want가 충족되었는지 체크
        if all(n <= 0 for n in want_dic.values()):
            cnt += 1
    
    # 하루씩 가장 지난날을 제거하고, 오는날을 추가
    for n, i in enumerate(discount[10:]):
        if i in want_dic:
            want_dic[i] -= 1
        if discount[n] in want_dic:
            want_dic[discount[n]] += 1
        
        # 모든 want가 충족되었는지 체크
        if all(n <= 0 for n in want_dic.values()):
           cnt += 1
    return cnt

# 입출력 예시
print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], 
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], 
               ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))