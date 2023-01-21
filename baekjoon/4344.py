# 문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
#
# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
#
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
#
# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

n_s = int(input())
lst2 = [list(map(int, input().split())) for _ in range(n_s)]
result = [0 for i in range(n_s)]
count = 0
for lst1 in lst2:
    avg = (sum(lst1[1:])) / lst1[0]
    num = 0
    for i in lst1[1:]:
        if i > avg:
            num += 1
    result[count] = num/lst1[0] * 100
    count += 1

for j in range(n_s):
    print(format(result[j], ".3f") + "%")




