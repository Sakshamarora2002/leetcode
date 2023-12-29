from itertools import chain, combinations

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count = 0
        covered = 0
        i = 0

        while covered < n:
            if i < len(nums) and nums[i] <= covered + 1:
                covered += nums[i]
                i += 1
            else:
                # Add the next uncovered number to the list
                covered += covered + 1
                count += 1

        return count

        