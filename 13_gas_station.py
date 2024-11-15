from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        last_gas = 0

        for i in range(len(gas)):
            last_gas += gas[i] - cost[i]

            if last_gas < 0:
                last_gas = 0
                start = i + 1
        return start


# Example usage
sol = Solution()

# Example inputs
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

# Call the function and print the result
print(sol.canCompleteCircuit(gas, cost))
