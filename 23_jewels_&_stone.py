class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        s=set(jewels)#makes into O(1)look up time
        count=0

        for stone in stones:
            if stone in s:#check if current stone is in set of jewels
                count+=1
        return count
s=Solution()
print(s.numJewelsInStones('aA','aAAbbbb'))

