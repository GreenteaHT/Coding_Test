-- https://school.programmers.co.kr/learn/courses/30/lessons/59412

SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR BETWEEN 9 AND 20
ORDER BY HOUR ASC