# https://school.programmers.co.kr/learn/courses/30/lessons/250137

def solution(bandage, health, attacks):
    current_time = 0
    max_health = health
    current_health = health
    cool_time = bandage[0]
    regen = bandage[1]
    heal = bandage[2]
    
    for atk in attacks:
        time_to_heal = atk[0] - current_time - 1
        current_health += time_to_heal * regen + time_to_heal // cool_time * heal
        if current_health > max_health:
            current_health = max_health
        current_health -= atk[1]
        # 체력이 0이 되면 종료
        if current_health <= 0 : 
            return -1
        current_time = atk[0]
        
    return current_health if current_health > 0 else -1

print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))