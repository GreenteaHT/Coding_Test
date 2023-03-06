# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    file_row_loc_lst, file_col_loc_lst = [], []
    for n_r, row in enumerate(wallpaper):
        for n_c, col in enumerate(row):
            if col == '#':
                file_row_loc_lst.append(n_r)
                file_col_loc_lst.append(n_c)
    answer = [min(file_row_loc_lst), min(file_col_loc_lst), max(file_row_loc_lst)+1, max(file_col_loc_lst)+1]
    return answer

# 입출력 예시
print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))