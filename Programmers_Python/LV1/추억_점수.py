# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearing, photo):
    name_dic = dict(zip(name, yearing))
    answer = []
    for i in photo:
        alu = 0
        for j in i:
            if j in name:
                alu += name_dic[j]
        answer.append(alu)
    print(name_dic)

    return answer

# 입출력 예시
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]]))
