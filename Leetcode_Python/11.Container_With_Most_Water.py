# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_water = 0

        while left_pointer < right_pointer:
            amount_of_water = min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer)
            max_water = max(max_water, amount_of_water)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_water
