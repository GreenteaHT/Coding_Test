# https://leetcode.com/problems/monotonic-array

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True

        is_increasing = False
        is_decreasing = False
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                is_increasing = True
            elif nums[i] > nums[i + 1]:
                is_decreasing = True

            if is_increasing and is_decreasing:
                return False

        return True
    