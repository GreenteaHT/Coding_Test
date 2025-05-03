# https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for idx in range(len(digits) - 1, -1, -1):
            carry, remain = divmod(digits[idx] + carry, 10)
            digits[idx] = remain
            if carry != 1:
                break
        
        if carry == 1:
            return [1] + digits

        return digits
    