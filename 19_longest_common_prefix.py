class Solution:
    def longestCommonPrefix(self, strs):

        res=""
                           #first word in the string
        for i in range(len(strs[0])):

            for s in strs:       #if the characters dont match
                if i==len(s) or  s[i]!=strs[0][i]:
                    return res
            res+=strs[0][i]
        return res
s=Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))