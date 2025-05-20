# https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0

        for char in t:
            if index >= len(s):
                return True

            if s[index] == char:
                index += 1
            
        return index == len(s)
            