from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        fuel = 0
        for num in nums:
            if fuel < 0:
                return False
            elif fuel < num:
                fuel = num
            fuel -= 1
        return True

# Hardcoded input
nums = [2, 3, 1, 1, 4]
solution = Solution()
print(solution.jump(nums))
