// https://leetcode.com/problems/remove-duplicates-from-sorted-array/description

var removeDuplicates = function(nums) {
    var dupleCount = 0;
    var lastNum = -101;
    for (let i = 0; i < nums.length; i++) {
        if (lastNum === nums[i]) {
            nums.splice(i, 1);
            dupleCount += 1;
            i--;
        } else {
            lastNum = nums[i];
        }
    };
    return nums.length
};