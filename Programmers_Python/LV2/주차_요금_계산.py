# https://school.programmers.co.kr/learn/courses/30/lessons/92341

def solution(fees, records):
    park_dic = {}  # 차량번호 : [상태, 입출 시간(분), 누적 시간(요금)]
    
    for r in records:  # records에 있는 기록 정산
        t, n, s = r.split()  # 시간, 차량번호, 상태
        t = int(t[:2]) * 60 + int(t[3:])  # 시간을 분으로 변환
        
        if n not in park_dic:  # 처음 들어오는 차량이면 딕셔너리에 추가
            park_dic[n] = [s, t, 0]  # [상태, 입출 시간(분), 누적 시간(요금)]
        else:
            # OUT일 때 누적 시간 갱신
            if park_dic[n][0] == "IN":
                park_dic[n][2] += t - park_dic[n][1]
            # 상태 갱신
            park_dic[n][1] = t
            park_dic[n][0] = s

    for i in park_dic:  # 나가지 않은 차들 정산
        # OUT일 때 누적 시간 갱신
        if park_dic[i][0] == "IN":
            park_dic[i][2] += 1439 - park_dic[i][1]
        # 상태 갱신(없어도 됨)
        park_dic[i][1] = 1439
        park_dic[i][0] = "OUT"
        
        # 누적 시간을 요금으로 변환
        park_dic[i][2] = fees[1] - ((fees[0] - park_dic[i][2]) // fees[2]) * fees[3] * (park_dic[i][2] > fees[0])
    return [item[1][2] for item in sorted(park_dic.items())]  # 정렬 후 value 특정값만 리스트로 작성

# 입출력 예시
print(solution([180, 5000, 10, 600], 
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], 
               ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))

# 추가 예시
print(solution([180, 5000, 10, 1000], ["05:59 0000 IN", "05:59 1111 IN"]))