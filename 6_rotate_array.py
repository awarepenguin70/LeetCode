from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Calculate the effective rotation steps
        k = k % len(nums)

        # Perform the rotation
        nums[:] = nums[-k:] + nums[:-k]

        # Return nums to show the output array
        return nums

# Test the function
s = Solution()
print(s.rotate([1, 2, 3, 4, 5, 6, 7], 3))  # Expected output: [5, 6, 7, 1, 2, 3, 4]
