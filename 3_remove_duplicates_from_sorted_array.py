class Solution:
    def removeDuplicates(self, nums):
        l=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[l]=nums[i]
                l+=1
        return l
nums = [1, 1, 2, 3, 3]
solution = Solution()
unique_count = solution.removeDuplicates(nums)

print("Number of unique elements:", unique_count)
print("Array after removing duplicates:", nums[:unique_count])