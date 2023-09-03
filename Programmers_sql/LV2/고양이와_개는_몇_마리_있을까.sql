-- https://school.programmers.co.kr/learn/courses/30/lessons/59040
-- 순서를 직접 정해 줄 수는 없는가?

SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC