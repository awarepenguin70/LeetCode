class Solution:
    def summaryRanges(self, nums):

        ans=[]
        i=0

        while i<len(nums):
            start=nums[i]

            while i<len(nums)-1 and nums[i]+1==nums[i+1]:
                i+=1
            if start!=nums[i]:
                ans.append(str(start)+"->"+str(nums[i]))
            else:
                ans.append(str(nums[i]))
            i+=1
        return ans
sol=Solution()
print(sol.summaryRanges([1,2,3,4,5,6,7,8,9,12,13,14]))
