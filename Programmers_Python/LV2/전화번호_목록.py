# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    #  딕셔너리 생성(key: 전화번호 길이, value: 전화번호)
    phone_book_dic = {}
    for i in phone_book:
        if len(i) in phone_book_dic:
            phone_book_dic[len(i)].add(i)
        else:
            phone_book_dic[len(i)] = {i}

    # 전화번호의 길이만 오름차순으로
    key_sort = sorted(phone_book_dic.keys())
    # j와 k는 전화번호의 길이를 nC2 순열로
    for j in range(len(key_sort)-1):
        for k in range(j+1, len(key_sort)):
            # k길이의 전화번호 목록을 가져와 전화번호 하나씩
            for number in phone_book_dic[key_sort[k]]:
                # 전화번호를 비교하기 쉽게 앞부분만 슬라이싱
                if number[:key_sort[j]] in phone_book_dic[key_sort[j]]:
                    # 같으면 false
                    return False
    return True

# 입출력 예시
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))