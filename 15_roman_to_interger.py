class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res


# Example usage
sol = Solution()

# Test cases
print(sol.romanToInt("III"))       # Output: 3
print(sol.romanToInt("IV"))        # Output: 4
print(sol.romanToInt("IX"))        # Output: 9
print(sol.romanToInt("LVIII"))     # Output: 58
print(sol.romanToInt("MCMXCIV"))   # Output: 1994
