# https://leetcode.com/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word for word in s.split(" ") if word != ""]
        return " ".join(words[::-1])
        