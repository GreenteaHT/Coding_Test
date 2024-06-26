-- https://school.programmers.co.kr/learn/courses/30/lessons/284527

SELECT G.SCORE, E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM HR_EMPLOYEES E LEFT JOIN
    (SELECT EMP_NO, SUM(SCORE) AS SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO
    ) AS G
    ON E.EMP_NO = G.EMP_NO
ORDER BY G.SCORE DESC
LIMIT 1