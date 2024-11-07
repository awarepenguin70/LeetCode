from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        smallest=0
        end,far=0,0
        n=len(nums)

        for i in range(n-1):
            far=max(far,i+nums[i])

            if i==end:
                smallest+=1
                end=far
        return smallest

sol = Solution()
print(sol.jump([3,2,3,1,1,4]))