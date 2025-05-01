# https://leetcode.com/problems/reverse-vowels-of-a-string/description

VOWELS = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

class Solution:
    def reverseVowels(self, s: str) -> str:
        string = list(s)
        vowels_order = [char for char in string if char in VOWELS]

        for idx, character in enumerate(string):
            if character in VOWELS:
                string[idx] = vowels_order.pop()
        
        return "".join(string)
            