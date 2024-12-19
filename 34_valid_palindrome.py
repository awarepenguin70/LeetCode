class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_char="".join(char.lower() for char in s if char.isalnum())
        return filtered_char == filtered_char[::-1]
s=Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))