from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        citations.sort()

        for i,v in enumerate(citations):
            if n-i<=v:
                return n-i
        return 0
sol=Solution()
print(sol.hIndex([3,0,6,1,5]))
