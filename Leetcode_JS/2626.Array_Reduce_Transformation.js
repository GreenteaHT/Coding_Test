// https://leetcode.com/problems/array-reduce-transformation/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    nums.forEach((num) => init = fn(init, num));
    return init;
};