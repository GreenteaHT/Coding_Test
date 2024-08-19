// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    // n번째와 n-2번째 수가 같으면 n번째를 제거
    for (let i = 2; i < nums.length; i++) {
        if (nums[i] === nums[i-2]) {
            nums.splice(i, 1);
            i--;
        }
    };
    return nums.length
};