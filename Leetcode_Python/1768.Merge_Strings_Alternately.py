# https://leetcode.com/problems/merge-strings-alternately/description

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1), len(word2))
        merged_string = ""

        for i in range(min_length):
            merged_string += word1[i] + word2[i]
        merged_string += word1[min_length:] + word2[min_length:]

        return merged_string
        