# https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        alu = 0

        for i in range(len(s)):
            current_value = symbol_value[s[i]]

            if i < len(s) - 1 and current_value < symbol_value[s[i + 1]]:
                alu -= current_value
            else:
                alu += current_value
            
        return alu
