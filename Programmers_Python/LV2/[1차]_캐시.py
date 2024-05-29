# https://school.programmers.co.kr/learn/courses/30/lessons/17680

from collections import OrderedDict

def solution(cacheSize, cities):
    if cacheSize == 0:  # 캐시가 없으면 과정 생략 결과 출력
        return 5 * len(cities)
    
    cache = OrderedDict()
    total_time = 0
    
    for city in cities:
        city = city.upper()  # 대소문자 구분없게 대문자로 갱신
        if city in cache:
            cache.move_to_end(city)  # 캐시 갱신
            total_time += 1
        else: 
            # 캐시에서 제일 오래 된 캐시 삭제
            if len(cache) >= cacheSize:
                cache.popitem(last=False)
            cache[city] = True
            total_time += 5

    return total_time

# 테스트
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 출력: 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))         # 출력: 21
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))  # 출력: 60
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))  # 출력: 52
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))  # 출력: 16