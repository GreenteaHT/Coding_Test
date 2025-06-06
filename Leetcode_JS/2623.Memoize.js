/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
  const memory = new Map();

  return function (...args) {
    const key = JSON.stringify(args);

    if (!memory.has(key)) {
      memory.set(key, fn(...args));
    }

    return memory.get(key);
  };
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */
