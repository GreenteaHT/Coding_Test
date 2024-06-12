from collections import Counter

def solution(weights):
    # 사람들의 목록은 많지만 몸무게의 인덱스가 적어서 counter로 정리하여 푸는것이 빠름
    weight_counter = Counter(weights)
    cnt = 0
    
    for weight in weight_counter:
        cnt += weight_counter[weight] * (weight_counter[weight] - 1) // 2
        if weight * 2 in weight_counter:
            cnt += weight_counter[weight * 2] * weight_counter[weight]
        if weight * 4 / 3 in weight_counter:
            cnt += weight_counter[weight * 4 / 3] * weight_counter[weight]
        if weight * 3 / 2 in weight_counter:
            cnt += weight_counter[weight * 3 / 2] * weight_counter[weight]
            
    return cnt

# 테스트
print(solution([100, 180, 360, 100, 270]))  # Output: 4