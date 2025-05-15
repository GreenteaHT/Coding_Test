// https://leetcode.com/problems/group-by

/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function (fn) {
  return this.reduce((acc, current) => {
    const key = fn(current);

    if (!Object.hasOwn(acc, key)) {
      acc[key] = [];
    }
    acc[key].push(current);

    return acc;
  }, {});
};
