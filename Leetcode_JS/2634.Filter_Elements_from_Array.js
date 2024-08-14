// https://leetcode.com/problems/filter-elements-from-array/description/

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    var arr2 = [];
    // index도 사용하는 경우가 있기 때문에
    // for문을 이용하여 하나씩 받아온 다음 조건문을 통해 arr2에 push를 진행
    for (var i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            arr2.push(arr[i]);
        };
    };
    return arr2;
};