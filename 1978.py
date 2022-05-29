# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
#
# 출력
# 주어진 수들 중 소수의 개수를 출력한다.
import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0  # 소수가 아님
    return 1  # 소수임

n = int(input())
lst1 = map(int, input().split())
count = 0
for i in lst1:
    if i == 1:
        continue
    count += is_prime_number(i)
print(count)


