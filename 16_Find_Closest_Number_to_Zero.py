from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return min(nums, key=lambda x: (abs(x), -x))

# Hardcoded input
nums = [-4, -2, 1, 4, 8]

# Instantiate the solution and get the result
solution = Solution()
result = solution.findClosestNumber(nums)

# Print the result
print("Closest number to zero:", result)
