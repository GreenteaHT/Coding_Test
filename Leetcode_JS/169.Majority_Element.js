// https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    var countNums = {};
    var maxNum = [0, 0];
    for (num of nums) {
        countNums[num] = (countNums[num] ?? 0) + 1;
    };

    return Object.keys(countNums).reduce((a, b) => countNums[a] > countNums[b] ? a : b);
};

// 카운트 도중에 조건문을 이용하여 최대 값을 기록하는 방법도 있음
// 이와 같은 경우는 전체적으로 한번만 순회하기 때문에 시간복잡도가 더 낮을 가능성이 존재
// var majorityElement = function(nums) {
//     let map = {};
//     let max = 0;
//     let res;

//     for(let x of nums) {
//         map[x] = (map[x] || 0) + 1;

//         if(map[x] >= max) {
//             res = x;
//             max = map[x];
//         }
//     }

//     return res;
// };