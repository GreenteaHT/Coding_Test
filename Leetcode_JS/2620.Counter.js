// https://leetcode.com/problems/counter/description/

/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function (n) {
  return function () {
    return n++;
  };
};

// 테스트
const counter = createCounter(10);
counter(); // 10
counter(); // 11
counter(); // 12
