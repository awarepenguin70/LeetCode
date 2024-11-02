from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[k-2]:
                nums[k]=nums[i]
                k+=1
        return k

nums = [1, 1, 2, 3, 3]
solution = Solution()
unique_count = solution.removeDuplicates(nums)

print("Number of unique elements:", unique_count)
print("Array after removing duplicates:", nums[:unique_count])