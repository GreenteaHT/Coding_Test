// https://leetcode.com/problems/function-composition/description/

/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function (functions) {
  return function (x) {
    return functions.reduceRight((acc, fn) => fn(acc), x);
  };
};

// 테스트
const fn = compose([(x) => x + 1, (x) => 2 * x]);
fn(4); // 9
