# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    lst1 = [0]
    lst2 = []
    for i in numbers:
        for j in lst1:
            lst2.append(j + i)
            lst2.append(j - i)
        lst1 = lst2.copy()
        lst2 = []
        print(lst1)
    print(lst1)
    
    return lst1.count(target)

# 입출력 예시
print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 2))