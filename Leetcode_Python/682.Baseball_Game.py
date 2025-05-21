# https://leetcode.com/problems/baseball-game

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        
        for o in operations:
            if o == "+":
                scores.append(scores[-1] + scores[-2])
            elif o == "D":
                scores.append(scores[-1] * 2)
            elif o == "C":
                del scores[-1]
            else:
                scores.append(int(o))

        return sum(scores)
