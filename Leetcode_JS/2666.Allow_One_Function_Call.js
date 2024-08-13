// https://leetcode.com/problems/allow-one-function-call/description/

/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    var used = false;
    return function(...args){
        if (!used) {
            used = true;
            return fn(...args);
        }
    }
};

// 테스트
let fn = (a,b,c) => (a + b + c)
let onceFn = once(fn)
onceFn(1,2,3); // 6
onceFn(2,3,6); // returns undefined without calling fn
