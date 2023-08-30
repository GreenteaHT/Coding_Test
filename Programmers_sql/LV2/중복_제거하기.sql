-- https://school.programmers.co.kr/learn/courses/30/lessons/59408
-- DISTINCT와 NOT NULL 사용 문제

SELECT COUNT(DISTINCT NAME) AS "count"
FROM ANIMAL_INS
WHERE NAME IS NOT NULL