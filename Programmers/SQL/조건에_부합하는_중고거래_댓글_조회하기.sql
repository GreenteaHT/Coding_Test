-- https://school.programmers.co.kr/learn/courses/30/lessons/164673

SELECT B.TITLE, 
    B.BOARD_ID, 
    R.REPLY_ID, 
    R.WRITER_ID, 
    R.CONTENTS, 
    DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD AS B, USED_GOODS_REPLY AS R
WHERE YEAR(B.CREATED_DATE) = 2022 AND
    MONTH(B.CREATED_DATE) = 10 AND
    B.BOARD_ID = R.BOARD_ID
ORDER BY R.CREATED_DATE ASC,
    B.TITLE ASC
    
