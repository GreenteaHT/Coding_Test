-- https://school.programmers.co.kr/learn/courses/30/lessons/157341?language=mysql

SELECT C.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR AS C
INNER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H ON C.CAR_ID = H.CAR_ID
WHERE C.CAR_TYPE = '세단' AND
    MONTH(START_DATE) = 10
GROUP BY C.CAR_ID
ORDER BY C.CAR_ID DESC