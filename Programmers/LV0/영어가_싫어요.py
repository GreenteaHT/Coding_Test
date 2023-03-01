# https://school.programmers.co.kr/learn/courses/30/lessons/120894

def solution(numbers):
    num_en = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_int = [str(i) for i in range(10)]
    for i in range(10):
        numbers = numbers.replace(num_en[i], num_int[i])
    return int(numbers)

# 입출력 예시
print(solution("onetwothreefourfivesixseveneightnine"))
print(solution("onefourzerosixseven"))