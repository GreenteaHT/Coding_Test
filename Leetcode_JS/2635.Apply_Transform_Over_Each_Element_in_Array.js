// https://leetcode.com/problems/apply-transform-over-each-element-in-array/submissions/1379468701/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    answer = []
    arr.forEach((number, index) => answer.push(fn(number, index)))
    return answer;
};