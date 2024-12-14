from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort acc to first number
        intervals.sort(key=lambda interval: interval[0])

        merged = []

        for interval in intervals: #not overlapping
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])#highest ending value of 2 intervals after merging
        return merged
sol=Solution()
print(sol.merge([[1,3],[2,6],[8,9]]))


