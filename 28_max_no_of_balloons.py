from collections import Counter


class Solution:
    def maxNoOfBalloons(self, text: str) -> int:

        counterText=Counter(text)
        balloon=Counter("balloon")

        res=len(text)

        for i in balloon:
            res=min(res,counterText[i]//balloon[i])
        return res
s=Solution()
print(s.maxNoOfBalloons("balddloonballoon"))