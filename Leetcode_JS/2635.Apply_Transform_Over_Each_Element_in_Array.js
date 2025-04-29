// https://leetcode.com/problems/apply-transform-over-each-element-in-array/description

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
  return arr.map((number, index) => fn(number, index));
};
