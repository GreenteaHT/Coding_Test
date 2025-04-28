# https://leetcode.com/problems/find-the-difference/description

from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        character_count_dict = defaultdict(int)

        for character in s:
            character_count_dict[character] += 1
        
        for character in t:
            if character_count_dict[character] == 0:
                return character
            character_count_dict[character] -= 1
