# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1

# 아래와 같은 find 함수로 풀이 할 수도 있다.
# def strStr(self, haystack: str, needle: str) -> int:
#     return haystack.find(needle)
