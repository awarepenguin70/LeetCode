from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]
        return s  # Optional: return the reversed list for visibility

sol = Solution()
string = list("hello")  # Convert the string to a list of characters
result = sol.reverseString(string)
print("".join(result))  # Convert the list back to a string for display
