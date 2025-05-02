# https://leetcode.com/problems/move-zeroes/description

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_position = 0

        for i, n in enumerate(nums):
            if n != 0:
                nums[insert_position] = nums[i]
                insert_position += 1

        for i in range(insert_position, len(nums)):
            nums[i] = 0
        """
        Do not return anything, modify nums in-place instead.
        """
