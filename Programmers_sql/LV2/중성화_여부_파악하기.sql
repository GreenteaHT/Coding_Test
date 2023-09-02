-- https://school.programmers.co.kr/learn/courses/30/lessons/59409

SELECT ANIMAL_ID, NAME, 
    CASE WHEN SEX_UPON_INTAKE LIKE '%Neutered%'
    OR SEX_UPON_INTAKE LIKE '%Spayed%' THEN 'O'
    ELSE 'X' 
    END AS 중성화
FROM ANIMAL_INS

-- 정규식 풀이
-- SELECT
--     ANIMAL_ID,
--     NAME,
--     IF(SEX_UPON_INTAKE REGEXP ('Neutered|Spayed'),'O','X') AS 중성화
-- FROM
--     ANIMAL_INS
-- ORDER BY
--     ANIMAL_ID