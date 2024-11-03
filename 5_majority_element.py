from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        for num, count in frequency.items():
            if count > len(nums) // 2:
                print(num)
# Test the function
solution = Solution()
print(solution.majorityElement([1, 1, 1, 2, 2, 3]))  # Output should be 1
