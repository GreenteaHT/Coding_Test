# https://school.programmers.co.kr/learn/courses/30/lessons/17677

# 중복도 가능하게 수정 할 것

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    str1_set = set(str1[i] + str1[i + 1] for i in range(len(str1) - 1) if
                'A' <= str1[i] <= 'Z' and 'A' <= str1[i + 1] <= 'Z')
    str2_set = set(str2[j] + str2[j + 1] for j in range(len(str2) - 1) if
                'A' <= str2[j] <= 'Z' and 'A' <= str2[j + 1] <= 'Z')
    print(str1_set, str2_set)
    return int(len(str1_set & str2_set) / 
               len(str1_set | str2_set) * 65536) if str1_set | str2_set else 65536

# 입출력 예시
print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))