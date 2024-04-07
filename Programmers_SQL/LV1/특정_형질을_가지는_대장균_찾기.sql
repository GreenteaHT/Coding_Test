-- https://school.programmers.co.kr/learn/courses/30/lessons/301646

SELECT COUNT(*) COUNT
FROM ECOLI_DATA
WHERE GENOTYPE & 5 AND
    NOT GENOTYPE & 2
