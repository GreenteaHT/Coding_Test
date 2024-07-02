# https://school.programmers.co.kr/learn/courses/30/lessons/12923

def solution(begin, end):
    answer = [1] * (end - begin + 1)
    
    # 1번째 자리는 0 고정
    if begin == 1:
        answer[0] = 0
        
    # 소인수의 최소값을 구해야하므로 (2부터 최대값의 제곱근)의 범위이용
    for i in range(int(end**(1/2)), 1, -1):
        # 소인수의 n배수만 갱신
        for j in range(max(i * i, (begin + i - 1) // i * i), end + 1, i):
            # 블록의 숫자를 넘어가는지 확인
            if j // i <= 10000000:
                answer[j - begin] = j // i 
            else:  # 소인수로 나눈값이 블록의 숫자를 넘어간다면 기존의 숫자와 소인수와 비교해 큰 값 갱신
                answer[j - begin] = max(answer[j - begin], i)
                
    return answer

# 테스트
print(solution(1, 10))
print(solution(2, 2))
print(solution(1, 20))
print(solution(9999990, 10000000))
print(solution(477559014, 477559014))
print(solution(100000015, 100000015))


