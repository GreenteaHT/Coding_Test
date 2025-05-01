# https://leetcode.com/problems/valid-anagram/description

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        charater_count = defaultdict(int)

        for character in s:
            charater_count[character] += 1

        for character in t:
            if charater_count[character] == 0:
                return False
            charater_count[character] -= 1

        return True

# Counter 함수를 이용하여 한번에 정리도 가능  
# from collections import Counter
