def solution(schedules, timelogs, startday):
    scheduled_minutes = [convert_to_minutes(time) for time in schedules]
    is_working_day = [True, True, True, True, True, False, False]
    compliant_employees = [True] * len(schedules)
    
    for day_offset in range(7):
        current_day = (startday + day_offset - 1) % 7
        
        if not is_working_day[current_day]:
            continue
            
        for emp_idx, is_compliant in enumerate(compliant_employees):
            if not is_compliant:
                continue
            
            actual_minutes = convert_to_minutes(timelogs[emp_idx][day_offset])
            allowed_minutes = scheduled_minutes[emp_idx] + 10
            
            if actual_minutes > allowed_minutes:
                compliant_employees[emp_idx] = False
    
    return sum(compliant_employees)

def convert_to_minutes(time):
    hours = time // 100
    minutes = time % 100
    return hours * 60 + minutes

# 입출력 예시
print(solution([700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5))
print(solution([730, 855, 700, 720], [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]], 1))