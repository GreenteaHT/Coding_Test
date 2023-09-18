-- https://school.programmers.co.kr/learn/courses/30/lessons/77487

SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN 
-- 서브쿼리를 이용해 HOST_ID로 그룹을 만들어주고 개수를 측정
    (SELECT HOST_ID
      FROM PLACES
      GROUP BY HOST_ID
      HAVING COUNT(*) >= 2)
ORDER BY ID ASC