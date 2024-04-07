-- https://school.programmers.co.kr/learn/courses/30/lessons/276034

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS D
WHERE EXISTS
    (SELECT CODE
    FROM SKILLCODES S
    WHERE D.SKILL_CODE & S.CODE != 0
    AND (S.NAME = 'Python' OR S.NAME = 'C#')
    )
ORDER BY ID
