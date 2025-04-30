# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest_number_of_candies = max(candies)
        return [candy + extraCandies >= greatest_number_of_candies for candy in candies]
        