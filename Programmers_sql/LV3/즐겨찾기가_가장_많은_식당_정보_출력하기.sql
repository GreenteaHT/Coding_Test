-- https://school.programmers.co.kr/learn/courses/30/lessons/131123

SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN (
    -- 서브 쿼리를 이용해 가장 즐겨찾기가 많은 식당만 고름
    SELECT FOOD_TYPE, MAX(FAVORITES)
    FROM REST_INFO
    GROUP BY FOOD_TYPE)
GROUP BY FOOD_TYPE
ORDER BY FOOD_TYPE DESC