-- https://school.programmers.co.kr/learn/courses/30/lessons/59411

SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS AS I
INNER JOIN ANIMAL_OUTS AS O ON I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY DATEDIFF(O.DATETIME, I.DATETIME) DESC
LIMIT 2