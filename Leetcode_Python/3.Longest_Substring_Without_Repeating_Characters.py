# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        longest_length = 0
        left_pointer = 0
        right_pointer = 0

        while (right_pointer < len(s)):
            if s[right_pointer] in characters:
                characters.remove(s[left_pointer])
                left_pointer += 1
            else:
                characters.add(s[right_pointer])
                right_pointer += 1
                longest_length = max(longest_length, len(characters))
        
        return longest_length
