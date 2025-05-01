// https://leetcode.com/problems/array-reduce-transformation/description

/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function (nums, fn, init) {
  nums.forEach((num) => (init = fn(init, num)));
  return init;
};

// reduce를 이용한 방법법
// var reduce = function(nums, fn, init) {
//     return nums.reduce((accumulator, currentValue) => fn(accumulator, currentValue), init)
// };
