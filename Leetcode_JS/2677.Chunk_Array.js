// https://leetcode.com/problems/chunk-array

/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function (arr, size) {
  const chunked_array = [];

  for (let i = 0; i < arr.length; i += size) {
    chunked_array.push(arr.slice(i, i + size));
  }

  return chunked_array;
};
