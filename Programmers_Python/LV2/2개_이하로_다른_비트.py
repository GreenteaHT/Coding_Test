# https://school.programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    for n in numbers:
        binary = "0" + bin(n)[2:]
        length = len(binary)
        for i in range(length-1, 0, -1):
            if binary[i] == "1" and binary[i-1] == "1":
                continue
            n += 2**(length-1-i)
            break
        answer.append(n)
    
    return answer

# 테스트
print(solution([2, 7, 5, 3]))


## 비트 연산자를 이용한 간단한 효율적인 풀이
# def solution(numbers):
#     answer = []
#     for val in numbers:
#         answer.append(((val ^ (val+1)) >> 2) +val +1)

#     return answer