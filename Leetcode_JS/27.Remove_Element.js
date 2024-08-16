// https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    var countVal = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === val) {
            nums.splice(i, 1);
            countVal += 1;
            i--;
        };
    };
    nums = [...nums, ...Array.from({length:countVal}, (v,i)=>"_")];
    return nums.length - countVal;
};

// nums도 저장해주어야 채점 프로그램이 참조함