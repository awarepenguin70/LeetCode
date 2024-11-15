from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        # Forward pass to satisfy the condition for higher-rated children
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Backward pass to satisfy the condition for higher-rated children
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

# Instantiate the solution class
sol = Solution()

# Example usage
ratings = [1, 0, 2]  # Replace with your desired input
print(sol.candy(ratings))
