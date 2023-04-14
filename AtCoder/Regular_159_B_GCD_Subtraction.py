from math import gcd

# 약수 목록을 반환하는 함수
def divisors_lst(n):
    lower_divisors, upper_divisors = [], []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
    return lower_divisors + upper_divisors[::-1]

# 입력 받기
A, B = map(int, input().split())
# cnt는 총 진행한 단계
cnt = 0
# A, B 순서로 오름차순 정렬
if A < B:
    A, B = B, A
# 1을 제외한 공약수 출력
div_lst = divisors_lst(A - B)[1:]

# A나 B가 0 이하가 되면 더 이상 gcd 뺄셈을 할 수 없음
while A > 0 and B > 0:
    g = gcd(A, B)
    A //= g
    B //= g
    n_m1 = B
    
    # gcd로 나눈 A와 B의 차가 공약수로 나누어지는지?
    for new_g in div_lst:
        # 나누어진다면 A가 새로운 예비 공약수로 나누어 질 수 있도록 t를 구함
        if (A - B) % new_g == 0:
            n_m1 = min(n_m1, A % new_g)
    
    # n_m1만큼 g가 1인 경우
    A -= n_m1
    B -= n_m1
    cnt += n_m1
    
print(cnt)

