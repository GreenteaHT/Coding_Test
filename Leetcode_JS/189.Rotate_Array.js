// https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    k %= nums.length;
    const answer = [...nums.slice(nums.length - k) , ...nums.slice(0, nums.length-k)];
    for (let i = 0; i < nums.length; i++) {
        nums[i] = answer[i]
    }
};

/*
nums에 직접적으로 할당할 수 없기 때문에 반복문으롤 요소들을 바꿔줌
*/