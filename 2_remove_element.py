from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Count the frequency of each element in the list
        frequency = Counter(nums)

        # Check for the element that appears more than len(nums) // 2 times
        for num, count in frequency.items():
            if count > len(nums) // 2:
                return num
        return None  # Return None if no majority element is found

# Test the function
solution = Solution()
print(solution.majorityElement([1, 1, 1, 2, 2, 3]))  # Expected output is 1


