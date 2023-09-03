# https://school.programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    str1_dic = gen_wrd_dic(str1)
    str2_dic = gen_wrd_dic(str2)
    
    n_inter = 0
    for i in str1_dic:
        if i in str2_dic:
            n_inter += min(str1_dic[i], str2_dic[i])

    n_union = sum(str1_dic.values()) + sum(str2_dic.values()) - n_inter
    return int((n_inter / n_union * 65536)) if n_union else 65536
    
def gen_wrd_dic(str):
    str = str.upper()
    str_dic = {}
    for i in range(len(str) - 1):
        if 'A' <= str[i] <= 'Z' and 'A' <= str[i + 1] <= 'Z':
            if str[i:i+2] in str_dic:
                str_dic[str[i:i+2]] += 1
            else:
                str_dic[str[i:i+2]] = 1
    return str_dic

# 입출력 예시
print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))